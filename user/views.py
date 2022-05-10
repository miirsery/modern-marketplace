# from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response


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
