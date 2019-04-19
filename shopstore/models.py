from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
	name=models.CharField(max_length=100,blank=True)
	image=models.ImageField(upload_to="image/item",blank=True)
	describe=models.CharField(max_length=300,blank=True)
	price=models.FloatField(default=0,blank=True)
	quantity=models.IntegerField(default=0,blank=True)
	date=models.DateField(blank=True)

class Transaction(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	item_id=models.CharField(max_length=200,blank=True)
	total=models.IntegerField(default=0,blank=True)
	datetime=models.DateTimeField(blank=True)

class ShopingCart(models.Model):
	item=models.ForeignKey(Item,on_delete=models.CASCADE)
	user_id=models.IntegerField(default=0,blank=True)
	datetime=models.DateTimeField(blank=True)
		