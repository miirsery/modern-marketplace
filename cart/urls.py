from django.urls import path
from .views import (
    CartAddProductApi,
    CartApiList,
    CalculationCartApiList,
)

urlpatterns = [
    path('add/', CartAddProductApi.as_view()),
    path('list-products-cart/', CartApiList.as_view()),
    path('update-final-price/', CalculationCartApiList.as_view()),
]
