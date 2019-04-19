from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from django.core import serializers
from .models import *
import datetime,re,random

# Create your views here.

def index(request):
	items=Item.objects.all()
	items=random.sample(list(items),len(items))
	return render(request,'shopstore/index.html',{'items':items})

def search(request):
    query=""
    if request.method=="GET" and request.GET.get('q',""):
        query=request.GET['q']
        items=Item.objects.filter(name__contains=query)
        items=random.sample(list(items),len(items))
        return render(request,'shopstore/search.html',{'items':items,'query':query})
    else:
        return redirect('/')

def dashboard(request):
	items=Item.objects.all()
	cartitems=ShopingCart.objects.filter(user_id=request.user.id)
	transactions=Transaction.objects.filter(user=request.user)
	transac=[]
	for x in transactions:
		x.item_id=len(x.item_id.split(','))
		transac.append(x)
	if request.method=='POST' and request.POST.get('clear_cart',""):
		shopingcarts=ShopingCart.objects.filter(user_id=request.user.id)
		for x in shopingcarts:
			x.delete()
		return redirect("/accounts/dashboard/")
	if request.method=='POST' and request.POST.get('purchase',""):
		item_ids=request.POST["purchase"]
		item_list=(item_ids.split(","))
		totalsum=0;

		for var in cartitems:
			for val in item_list:
				if var.item.id==int(val):
					totalsum=totalsum+var.item.price
		print("transactions sum is $ ",totalsum)
		shopingcarts=ShopingCart.objects.filter(user_id=request.user.id)
		try:
			Transaction.objects.create(user=request.user,item_id=item_ids,total=totalsum,datetime=datetime.datetime.now())
			for x in shopingcarts:
				x.delete()
		except Exception as e:
			pass
		return redirect("/accounts/dashboard/")
	return render(request,'shopstore/dashboard.html',{'items':items,'cartitems':cartitems,'transactions':transac})

def itemdetails(request,item_id):
	has_transac=False
	item=Item.objects.get(id=item_id)
	userauth=None
	if request.user.is_authenticated:
			userauth=True

	try:
		transactions=Transaction.objects.filter(user=request.user)
	except Exception as e:
		transactions=None
	if transactions:
		for x in transactions:
			y=x.item_id.split(',')
			for z in y:
				if z==item_id:
					has_transac=True

	try:
		is_in_cart=ShopingCart.objects.get(item=Item.objects.get(id=item_id),user_id=request.user.id)
	except Exception as e:
		is_in_cart=None

	if request.method=='POST' and request.POST.get('buy',""):
		if userauth:
		    return redirect("/item/details/%s/"%item_id)
	if request.method=='POST' and request.POST.get('cart',""):
		if userauth:
			ShopingCart.objects.create(item=Item.objects.get(id=item_id),user_id=request.user.id,datetime=datetime.datetime.now())
			return redirect("/item/details/%s/"%item_id)
	return render(request,'shopstore/itemdetails.html',{'userauth':userauth,'item':item,'has_transac':has_transac,'is_in_cart':is_in_cart})

def login_view(request):
	loginerrors=[]
	signuperrors=[]
	username=""
	user=None

	if request.method=='POST' and request.POST.get('login',""):
		username=request.POST['username']
		password=request.POST['password']

		try:
			user=User.objects.get(username=username)
		except:
			pass

		if user:
			checkuser=authenticate(username=user.username,password=password)
		else:
			checkuser=None

		if checkuser is not None and checkuser.is_active:
			try:
			    login(request,checkuser)
			    #request.session[str(user.id)]="is_active"
			    return redirect("/")
			except:
			    loginerrors.append("Internal Server Error.")
		else:
			loginerrors.append("Invalid username or password.")

	if request.method=='POST' and request.POST.get('register',""):
		password=request.POST['password']
		username=request.POST['username']

		try:
			User.objects.get(username=username)
			signuperrors.append("Username already taken.")
		except Exception as e:
			pass

		if not signuperrors:
			try:
				user=User.objects.create_user(username=username,password=password)
				user.is_staff=True
				user.save()
				#Profile.objects.create(user=user)
				#UserTracker.objects.create(user=user,last_seen=datetime.datetime.now())
				return redirect("/accounts/login/")
			except:
				signuperrors.append("Internal Server Error. Contact Admin.")
	return render(request,'shopstore/login.html',{'loginerrors':loginerrors,'signuperrors':signuperrors,})

def logout_view(request):
	shopingcarts=ShopingCart.objects.filter(user_id=request.user.id)
	for x in shopingcarts:
		x.delete()
	logout(request)
	return redirect('/')
