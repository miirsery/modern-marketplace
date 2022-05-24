from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.response import Response
from .models import Cart
from product.models import Product
from .serializers import AddToCartSerializer
from product.serializers import ProductSerializer
from rest_framework import status


class CartAddProduct(APIView):
    serializer_class = AddToCartSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data.get('product_id')
        prod_obj = Product.objects.get(id=product_id)

        if user in prod_obj.basket.all():
            prod_obj.basket.remove(user)
        else:
            prod_obj.basket.add(user)

        basket, created = Cart.objects.get_or_create(
            user_name_id=user.id, product_name_id=product_id
        )

        basket.save()
        return Response(prod_obj.basket.all().count())
