from rest_framework import serializers
from .models import (
    Category,
    Product,
    # SetCharacteristics,
    # ItemCharacteristics,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id', 'title',
        )


class ProductSerializer(serializers.ModelSerializer):
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
