from rest_framework import generics, viewsets
from .serializers import (
    CategorySerializer,
    ProductSerializer,
)
from .models import (
    Category,
    Product,
)

# Create your views here.


class ProductViewSetAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ListCategoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
