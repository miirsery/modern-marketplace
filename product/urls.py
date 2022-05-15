from django.urls import path, include
from .views import (
    ListCategoryApiView,
    ProductViewSetAPI,
)
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'product-info', ProductViewSetAPI)

urlpatterns = [
    path('list-category/', ListCategoryApiView.as_view()),
    path('v1/', include(router.urls)),
]
