from django.views import generic
from Users.models import Poco_User
from Users.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer

from django.shortcuts import get_object_or_404, redirect

class UserList(generics.ListAPIView):
    
    queryset= Poco_User.objects.all()
    serializer_class = UserSerializer


class UserCreation(generics.CreateAPIView):
    serializer_class = UserSerializer




