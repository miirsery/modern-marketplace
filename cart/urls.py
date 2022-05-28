from django.urls import path
from .views import (
    CartAddProductApi,
    CartApiList,
)

urlpatterns = [
    path('add/', CartAddProductApi.as_view()),
    path('list-products-cart/', CartApiList.as_view()),
]
