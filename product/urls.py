from django.urls import path
from .views import (
    ListCategegoryApiView,
)

urlpatterns = [
    path('list-product/', ListCategegoryApiView.as_view()),
]
