'''
Created on May 17, 2011

@author: Hong Phi
'''
from django.contrib import admin
from models import Product, Comment


class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name', 'image', 'point', 'price', 'details']
    list_filter = ('point', 'price')
    search_fields = ('product_name', 'price')

class AdminComments(admin.ModelAdmin):
    list_display = ['comment_id', 'comment_user', 'comment_product', 'comment_date', 'comment_content']
    list_filter = ('comment_product', 'comment_user', 'comment_date')
    
admin.site.register(Product, AdminProduct)
admin.site.register(Comment, AdminComments)
