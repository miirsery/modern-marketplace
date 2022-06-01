from django.urls import path, include
from .views import (
    ListCategoryApiView,
    ProductViewSetAPI,
    ListApiProductByCategory,
    AddFavoriteProductApiView,
    FavoriteProductApiList,
    GetQuantityProductFavoriteApi,
)
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'product-info', ProductViewSetAPI)

urlpatterns = [
    path('list-category/', ListCategoryApiView.as_view()),
    path('v1/', include(router.urls)),
    path('catalog/<slug:slug_category>/', ListApiProductByCategory.as_view()),
    path(
        'favorite/add-product/',
        AddFavoriteProductApiView.as_view()
    ),
    path(
        'favorite/list-products/',
        FavoriteProductApiList.as_view()
    ),
    path(
        'favorite/quantity-products/',
        GetQuantityProductFavoriteApi.as_view()
    ),
]
