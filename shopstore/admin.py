from django.contrib import admin
from .models import *

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
	list_display=['name','describe','price','date']

class TransactionAdmin(admin.ModelAdmin):
	list_display=['user','item_id','total','datetime']

class ShopingCartAdmin(admin.ModelAdmin):
	list_display=['item','user_id','datetime']

admin.site.register(Item,ItemAdmin)
admin.site.register(Transaction,TransactionAdmin)
admin.site.register(ShopingCart,ShopingCartAdmin)