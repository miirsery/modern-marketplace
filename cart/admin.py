from django.contrib import admin
from .models import (
    Cart,
)


class CartAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'product_name',
        'user_name',
    )
    list_display_links = ('id',)
    search_fields = ('id', 'user_name',)


admin.site.register(Cart, CartAdmin)
