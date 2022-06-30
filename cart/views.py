from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import (
    Cart,
    CartProduct,
)
from product.models import Product
from .serializers import (
    AddToCartSerializer,
    ProductBasketSerializer,
    DeleteProductFromCartSerializer,
)
from .services.basket_calculator import BasketCalculator


class CartAddProductApi(APIView):
    serializer_class = AddToCartSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        """
        Добавление продукта в корзину.
        """
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

        return Response(
            {"count_products_in_basket": cart.total_products}
        )

    def patch(self, request, *args, **kwargs):
        """
        Изменение количества товара в корзине
        """
        user = request.user
        product_id = request.data.get('product_id')
        cart_product = CartProduct.objects.get(id=product_id)
        cart = Cart.objects.filter(user_name=user).first()
        new_count_products = request.data.get('new_count_products')
        cart_product.count_product = int(new_count_products)
        cart_product.save()
        basket_calculator = BasketCalculator()
        basket_calculator.basket_calculation(cart)
        cart.save()
        return Response(
            {"count_products_in_basket": cart.total_products}
        )


class DeleteFromCartApi(APIView):
    """
    Удаление продукта из корзины.
    """
    serializer_class = DeleteProductFromCartSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        product_del_id = request.data.get('product_id')
        cart = Cart.objects.filter(user_name=user).first()
        cart_product = CartProduct.objects.get(id=product_del_id)
        cart.products.remove(cart_product)
        cart_product.delete()
        return Response(
            {"count_products_in_basket": cart.total_products}
        )


class CartApiList(APIView):
    """
    Получение продуктов находящихся в корзине.
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        cart = Cart.objects.get(user_name=f"{self.request.user.id}")
        serializer = ProductBasketSerializer(cart)
        return Response(serializer.data)
