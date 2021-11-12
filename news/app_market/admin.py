from django.contrib import admin
from app_market.models import Shop, Product, CartProduct, Cart

class ShopAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Shop, ShopAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'number')

admin.site.register(Product, ProductAdmin)

'''
class CartAdmin(admin.ModelAdmin):
    list_display = ('quantity', 'total')

admin.site.register(Cart, CartAdmin)
'''


class CartAdmin(admin.ModelAdmin):
    list_display = ('product', 'final_price')

admin.site.register(Cart, CartAdmin)


class CartProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'final_price')

admin.site.register(CartProduct, CartProductAdmin)
