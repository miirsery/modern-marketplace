from django.urls import path, include
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .views import (
    UserCreateApiView,
    UserUpdateApiView,
    UserPasswordResetView,
    UserDeleteAvatarView,
)

urlpatterns = [
    path('register/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('token-create/', obtain_jwt_token, name='obtain_jwt_token'),
    path('authorization/', UserCreateApiView.as_view()),
    path('update/<int:pk>/', UserUpdateApiView.as_view()),
    url(
        r'^reset/password/reset/confirm/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$',
        UserPasswordResetView.as_view(),
    ),
    path('delete/avatar/', UserDeleteAvatarView.as_view())
]
