'''
Created on May 17, 2011

@author: Hong Phi
'''
from django.contrib import admin
from models import Product

class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name', 'image', 'point', 'price', 'details']
    list_filter = ('point', 'price')
    search_fields = ('product_name', 'price')

admin.site.register(Product, AdminProduct)
