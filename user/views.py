# from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserCreateApiView(APIView):
    queryset = User.objects.filter(is_active=True)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        request.data.copy()
        return Response(UserSerializer(request.user,
                                       context={"request": request}).data)


class UserUpdateApiView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


class UserPasswordResetView(APIView):
    def post(self, request, uid, token):
        post_data = {'uid': uid, 'token': token}
        return Response(post_data)


class UserDeleteAvatarView(APIView):
    queryset = User.objects.filter(is_active=True)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        user.avatar.delete(save=False)
        user.avatar = 'system_images/defult.jpg'
        user.save()
        return Response(
            UserSerializer(user, context={"request": request}).data,
            status.HTTP_200_OK
        )
