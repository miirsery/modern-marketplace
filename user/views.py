from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import (
    UserSerializer,
    UserInfoSerializer,
)
from .services.user_worker import UserWorker


class UserCreateApiView(APIView):
    """
    Авторизация пользователя.
    """
    queryset = User.objects.filter(is_active=True)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        request.data.copy()
        return Response(UserSerializer(request.user,
                                       context={"request": request}).data)


class UserUpdateApiView(generics.UpdateAPIView):
    """
    Обновление фото пользователя и логина.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserDeleteAvatarView(APIView):
    """
    Удаление фото аватара пользователя,
    установка default фото для аватара.
    """
    queryset = User.objects.filter(is_active=True)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        user_worker = UserWorker()
        user_worker.user_delete_avatar(user, 'system_images/defult.jpg')
        user.save()
        return Response(
            UserSerializer(user, context={"request": request}).data,
            status.HTTP_200_OK
        )


class AboutUserView(APIView):
    """
    Получение информации о пользоватле
    """
    queryset = User.objects.filter(is_active=True)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response(
            UserInfoSerializer(user, context={"request": request}).data,
            status.HTTP_200_OK
        )
