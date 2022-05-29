from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from .models import (
    Cart,
    CartProduct,
)
from product.models import Product
from .serializers import (
    AddToCartSerializer,
    ProductBasketSerializer,
)
from django.db.models import Sum
from .base.services import BasketСontroller


class CartAddProductApi(APIView):
    serializer_class = AddToCartSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data.get('product_id')
        prod_obj = Product.objects.get(id=product_id)
        count_products = request.data.get('count_product')
        cart = Cart.objects.filter(user_name=user).first()
        if not cart:
            cart = Cart.objects.create(user_name=user)
        cart_product, created = CartProduct.objects.get_or_create(
            cart=cart, product_name=prod_obj, count_product=int(count_products)
        )
        if created:
            cart.products.add(cart_product)
        return Response({"count_products": cart.products.count()})


class CartApiList(generics.ListAPIView):
    serializer_class = ProductBasketSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Cart.objects.filter(user_name=f"{self.request.user.id}")


class CalculationCartApiList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = request.user
        cart = Cart.objects.filter(user_name=user).first()
        basket_сontroller = BasketСontroller()
        basket_сontroller.calculation_final_basket_price(cart)
        basket_сontroller.calculation_total_products(cart)
        return Response(cart.products.values_list(
            'final_price', flat=True
        ).aggregate(Sum('final_price')))
