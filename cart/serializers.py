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


class DeleteProductFromCart(serializers.ModelSerializer):

    class Meta:
        model = CartProduct
        fields = (
            'cart', 'product_name',
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
            'price_now', 'price_old', 'quantity',
            'discounted_price', 'guarantee',
            'photo', 'colors',
            'slug',
        )


class CartProductSerializer(serializers.ModelSerializer):
    product_name = ProductInBasket()

    class Meta:
        model = CartProduct
        fields = (
            'id', 'final_price', 'product_name',
            'count_product',
            'final_total_discount',
            'final_price_not_discount',
        )


class ProductBasketSerializer(serializers.ModelSerializer):
    products = CartProductSerializer(many=True, required=False)

    class Meta:
        model = Cart
        fields = (
            'products', 'user_name',
            'total_products', 'final_price_cart',
            'total_discount_price', 'total_not_discount_price'
        )


class CartProductUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProduct
        fields = (
            'count_product',
        )
