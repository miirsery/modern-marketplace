from django.urls import path
from .views import (
    # CartApiView,
    CartAddProduct,
)

urlpatterns = [
    path('add/', CartAddProduct.as_view()),
]
