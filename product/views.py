from rest_framework import generics, viewsets
from .serializers import (
    CategorySerializer,
    ProductSerializer,
)
from .models import (
    Category,
    Product,
)
from rest_framework import permissions
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
