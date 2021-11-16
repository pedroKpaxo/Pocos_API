from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import permissions
# Create your views here.
from Wells.models import Well,User_Well
from Wells.serializers import WellSerializer,UserWellSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from Helpers.pagination import CustomPageNumberPagination
from Helpers.OwnerPermission import IsOwnerOrReadOnly

class WellList(generics.ListAPIView):
    """
    Retrieve,  all the well instances.
    """
    
    queryset= Well.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # - Serializer
    serializer_class = WellSerializer

    # - The filters 
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # - Custom Pagination,
    pagination_class = CustomPageNumberPagination
    filterset_fields = ['bacia', 'estado','municipio']
    

class WellDetail(APIView):
    """
    Retrieve,  well instance.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Well.objects.get(pk=pk)
        except Well.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        '''
        Gets a single Well fronm the main list
        '''
        well = self.get_object(pk)
        serializer = WellSerializer(well)
        return Response(serializer.data)

class User_WellList(generics.ListAPIView):
    """
    Retrieve,  all the well instances created by our users.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset= User_Well.objects.all()

    # - Serializer
    serializer_class = UserWellSerializer

    # - The filters 
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # - Custom Pagination,
    pagination_class = CustomPageNumberPagination
    filterset_fields = ['bacia', 'estado','municipio','owner']

class Create_User_Well(generics.CreateAPIView):
    """
    Retrieve,  well instance.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserWellSerializer

class Update_User_well(generics.RetrieveUpdateDestroyAPIView):
    '''
    CRUD VIEW for updating and deleting
    '''
    serializer_class= UserWellSerializer
    permission_class = IsOwnerOrReadOnly