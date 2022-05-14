from django.urls import path
from .views import (
    ListCategegoryApiView,
    ListProductApiView,
    CreateProductAPIView,
    UpdateProductAPIView,
)

urlpatterns = [
    path('list-category/', ListCategegoryApiView.as_view()),
    path('list-product/', ListProductApiView.as_view()),
    path('create-product/', CreateProductAPIView.as_view()),
    path(
        'update-product/<slug:slug>-<int:pk>/', UpdateProductAPIView.as_view()
    ),
]
