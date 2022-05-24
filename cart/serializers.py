from rest_framework import serializers
# from product.models import Product
from .models import Cart


class AddToCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = (
            'id', 'product_name',
            'user_name',
        )
