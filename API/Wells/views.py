from django.shortcuts import render

# Create your views here.
from Wells.models import Well
from Wells.serializers import WellSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

class WellList(generics.ListAPIView):
    
    queryset= Well.objects.all()
    serializer_class = WellSerializer

    


class WellDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Well.objects.get(pk=pk)
        except Well.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        well = self.get_object(pk)
        serializer = WellSerializer(well)
        return Response(serializer.data)