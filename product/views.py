from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from .serializers import (
    CategorySerializer,
    ProductSerializer,
)
from .models import (
    Category,
    Product,
    FavoriteUserProduct,
)
from .permissions import MyPermissions

# imports for 2 options for the output of goods by category through filters
# from rest_framework import filters
# from django_filters.rest_framework import DjangoFilterBackend
# import django_filters
# Create your views here.


class ProductViewSetAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in [
                'create', 'update', 'partial_update', 'destroy', 'list'
        ]:
            self.permission_classes = [MyPermissions]
        elif self.action in ['list']:
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super(self.__class__, self).get_permissions()


class ListCategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListApiProductByCategory(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        slug_category = self.kwargs['slug_category']
        return Product.objects.filter(category__slug_category=slug_category)


# the second option is to display products by category through filters
# class ListProductByCategory(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['category__slug_category']


class AddFavoriteProductApiView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        product_id = request.data.get('product_id')
        prod_obj = Product.objects.get(id=product_id)
        if user in prod_obj.favorite_product.all():
            prod_obj.favorite_product.remove(user)
        else:
            prod_obj.favorite_product.add(user)
        favorite_product, created = FavoriteUserProduct.objects.get_or_create(
            favorite_product_user=user, product_in_favorite_id=product_id
        )

        favorite_product.save()
        return Response({
            "count_favorite_products": user.favorite_products.all().count()
        })


class FavoriteProductApiList(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.request.user.favorite_products.all()
