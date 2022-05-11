from django.contrib import admin
from .models import (
    Product,
    Category,
    ProductImage,
    ProductColor,
)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)
    search_fields = ('id', 'title',)
    # list_editable = ('moderation',)
    list_filter = ('moderation',)
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(ProductColor)
