from django.shortcuts import render
from rest_framework import viewsets
from . serializers import *
from . models import *



class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
