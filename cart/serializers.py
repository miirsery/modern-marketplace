from rest_framework import serializers
from product.models import (
    Product,
)
from .models import (
    CartProduct,
    Cart,
)
from product.serializers import (
    PhotoProductSerializer,
    ColorProductSerializer,
)


class AddToCartSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartProduct
        fields = (
            'cart', 'product_name',
            'count_product',
        )


class ProductInBasket(serializers.ModelSerializer):
    photo = PhotoProductSerializer(many=True, required=False)
    colors = ColorProductSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = (
            'title', 'description',
            'price_now', 'price_old',
            'discounted_price', 'guarantee',
            'photo', 'colors',
            'slug',
        )


class CartProductSerializer(serializers.ModelSerializer):
    product_name = ProductInBasket()

    class Meta:
        model = CartProduct
        fields = (
            'final_price', 'product_name',
            'count_product',
        )


class ProductBasketSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(many=True, required=False)

    class Meta:
        model = Cart
        fields = (
            'products', 'user_name',
            'total_products', 'final_price_cart'
        )
