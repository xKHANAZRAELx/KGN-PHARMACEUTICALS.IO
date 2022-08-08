from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.alogin import Alogin

admin.site.register(Alogin)

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']



class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','phone']

class AdminOrders(admin.ModelAdmin):
    list_display=['product','customer','quantity','price','address','phone','date','status']

# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category , AdminCategory)
admin.site.register(Customer,AdminCustomer)
admin.site.register(Order,AdminOrders)

