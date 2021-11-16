from rest_framework import serializers

from Wells.models import Well

class WellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Well
        fields = ['id', 'bacia', 'estado', 'municipio', 'lat', 'long','formac']
    