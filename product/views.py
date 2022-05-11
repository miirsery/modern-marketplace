# from django.shortcuts import render
from rest_framework import generics
from .serializers import (
    CategorySerializer,
)
from .models import (
    Category,
)

# Create your views here.


class ListCategegoryApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
