from django.views import generic
from Users.models import CustomPocoUser
from Users.serializers import UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import permissions

from django.shortcuts import get_object_or_404, redirect

class UserList(generics.ListAPIView):
    '''
    View for all the Users.
    '''
    permission_classes = [permissions.IsAdminUser]
    
    queryset= CustomPocoUser.objects.all()
    serializer_class = UserSerializer


class UserCreation(generics.CreateAPIView):
    '''
    View for creating an user.

    '''
    permission_classes = [permissions.IsAdminUser]
    serializer_class = UserSerializer




