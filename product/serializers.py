from rest_framework import serializers
from .models import (
    Category,
    Product,
    ProductImage,
    ProductColor,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'category_name', 'slug_category',
        )


class PhotoProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ColorProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductColor
        fields = ('color',)


class ProductSerializer(serializers.ModelSerializer):
    photo = PhotoProductSerializer(many=True, required=False)
    category = CategorySerializer()
    colors = ColorProductSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = (
            'id', 'title', 'description',
            'price_now', 'price_old',
            'discounted_price', 'guarantee',
            'quantity', 'year', 'status', 'photo',
            'category', 'colors', 'characteristics',
            'slug',
        )
