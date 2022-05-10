from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token
from .views import (
    UserCreateAPIView,
)

urlpatterns = [
    path('register/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('token-create/', obtain_jwt_token, name='obtain_jwt_token'),
    path('authorization/', UserCreateAPIView.as_view()),
]
