from django.urls import path
from .views import (
    CartAddProductApi,
    CartApiList,
    CalculationCartApiList,
    CartUpdateCartProductApiView,
    CartDeleteCartProductApiView,
)

urlpatterns = [
    path('add/', CartAddProductApi.as_view()),
    path('list-products-cart/', CartApiList.as_view()),
    path('update-final-price/', CalculationCartApiList.as_view()),
    path(
        'update-cart-products/<int:pk>/',
        CartUpdateCartProductApiView.as_view()
    ),
    path(
        'delete-cart-products/<int:pk>/',
        CartDeleteCartProductApiView.as_view()
    ),
]
