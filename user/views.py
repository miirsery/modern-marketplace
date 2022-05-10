# from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response


class UserCreateAPIView(APIView):
    queryset = User.objects.filter(is_active=True)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        request.data.copy()
        return Response(UserSerializer(request.user,
                                       context={"request": request}).data)
