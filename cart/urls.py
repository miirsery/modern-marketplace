from django.urls import path
from .views import (
    CartAddProductApi,
    CartApiList,
    DeleteFromCartApi,
    UpdateQtyProductNotDirectlyCartApi,
)

urlpatterns = [
    path('add-product-in-cart/', CartAddProductApi.as_view()),
    path('delete-product-in-cart/', DeleteFromCartApi.as_view()),
    path('list-products-cart/', CartApiList.as_view()),
    path(
        'update-count-products-no-directly-cart/',
        UpdateQtyProductNotDirectlyCartApi.as_view()
    ),
]
