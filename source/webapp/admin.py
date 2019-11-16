from django.contrib import admin
from webapp.models import Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'order_description', 'rating')
    list_filter = ('rating',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)