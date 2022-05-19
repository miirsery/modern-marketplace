from rest_framework import serializers
from .models import (
    Category,
    Product,
    ProductImage,
    # SetCharacteristics,
    # ItemCharacteristics,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'title',
        )


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image',)


class ProductSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = (
            'title', 'description',
            'price_now', 'price_old',
            'discounted_price', 'guarantee',
            'quantity', 'year', 'status', 'photo',
            'category', 'color', 'characteristics',
            'slug',
        )
