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
    CartProductUpdateSerializer,
)
from .services.basket_calculator import BasketCalculator


class CartAddProductApi(APIView):
    """
    Добавление продукта в корзину.
    """
    serializer_class = AddToCartSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data.get('product_id')
        prod_obj = Product.objects.get(id=product_id)
        count_products = request.data.get('count_product')
        cart = Cart.objects.filter(user_name=user).first()

        if not cart:
            cart = Cart.objects.create(user_name=user,)

        cart_products_all_title = cart.products.all().values_list(
            'product_name__title', flat=True
        )

        if prod_obj.title in cart_products_all_title:
            return Response({"error": "Уже имеется в корзине"})

        cart_product, created = CartProduct.objects.get_or_create(
            cart=cart, product_name=prod_obj,
            count_product=int(count_products),
        )

        if created:
            cart.products.add(cart_product)

        return Response({"count_products": cart.products.count()})


class CartApiList(APIView):
    """
    Получение продуктов находящихся в корзине.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user_name=f"{self.request.user.id}")
        serializer = ProductBasketSerializer(cart)
        return Response(serializer.data)


class CalculationCartApiList(APIView):
    """
    Расчеты внутри корзины
    (Общая цена корзины, всего количества товаров в корзине и т.д).
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = request.user
        cart = Cart.objects.filter(user_name=user).first()
        basket_calculator = BasketCalculator()
        basket_calculator.final_basket_price(cart)
        basket_calculator.total_products(cart)
        basket_calculator.total_discount_products(cart)
        basket_calculator.total_price_not_discount_products(cart)
        return Response({"update_cart": True})


class CartUpdateCartProductApiView(generics.UpdateAPIView):
    """
    Обновление информации в корзине,
    в основном количество определённого товара.
    """
    queryset = CartProduct.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CartProductUpdateSerializer


class DeleteCartProductApiView(generics.DestroyAPIView):
    """
    Удаление товара из корзины.
    """
    queryset = CartProduct.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CartProductUpdateSerializer
