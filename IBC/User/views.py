from django.shortcuts import render
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
