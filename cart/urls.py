from django.urls import path
from .views import (
    CartAddProductApi,
    CartApiList,
    CalculationCartApiList,
    CartUpdateCartProductApiView,
    DeleteCartProductApiView,
)

urlpatterns = [
    path('add/', CartAddProductApi.as_view()),
    path('list-products-cart/', CartApiList.as_view()),
    path('update-calculations-cart/', CalculationCartApiList.as_view()),
    path(
        'update-cart-products/<int:pk>/',
        CartUpdateCartProductApiView.as_view()
    ),
    path(
        'delete-cart-products/<int:pk>/',
        DeleteCartProductApiView.as_view()
    ),
]
