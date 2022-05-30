from django.urls import path
from .views import (
    CartAddProductApi,
    CartApiList,
    CalculationCartApiList,
    CartUpdateApiView,
)

urlpatterns = [
    path('add/', CartAddProductApi.as_view()),
    path('list-products-cart/', CartApiList.as_view()),
    path('update-final-price/', CalculationCartApiList.as_view()),
    path('update-cart-products/<int:pk>/', CartUpdateApiView.as_view()),
]
