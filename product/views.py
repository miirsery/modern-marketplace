from rest_framework import generics
from .serializers import (
    CategorySerializer,
    ProductSerializer,
)
from .models import (
    Category,
    Product,
)

# Create your views here.


class ListCategegoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ListProductApiView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CreateProductAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
