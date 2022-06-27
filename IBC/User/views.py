from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer, UserCreateSerializer

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from .models import User


class UserViewSet(ModelViewSet):
    ttp_method_names = ['get', 'post', 'patch', 'delete']
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.method == "PATCH" or self.request.method == "POST":
            return UserCreateSerializer
        return UserSerializer

    @action(detail=False, methods=["GET", "PUT"])
    def current(self, request):
        user = User.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            print("GET :",request.user)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        elif request.method == 'PUT':
            print("PUT")
            serializer = UserSerializer(user, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
