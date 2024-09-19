from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
# Create your views here.


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer



