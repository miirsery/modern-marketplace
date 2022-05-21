from django.contrib import admin
from .models import (
    Product,
    Category,
    ProductImage,
    ProductColor,
)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title',
        'price_now', 'created_at',
        'updated_at', 'moderation',
        'guarantee', 'quantity',
        'year', 'status', 'category',
        'slug',
    )
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title', 'category',)
    list_editable = ('moderation',)
    list_filter = ('moderation', 'status',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(ProductColor)
