from django.contrib import admin
from .models import (
    Cart,
    CartProduct,
)


class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user_name', 'total_products',
        'final_price_cart',
    )
    list_display_links = ('user_name',)
    search_fields = ('id', 'user_name',)


class CartProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'cart', 'product_name',
        'count_product', 'final_price',
    )
    list_display_links = ('product_name',)
    search_fields = ('id', 'product_name',)


admin.site.register(Cart, CartAdmin)
admin.site.register(CartProduct, CartProductAdmin)
