from rest_framework import serializers

from Wells.models import Well, User_Well

class WellSerializer(serializers.ModelSerializer):
    '''
    Basic serializer class for the Well Model, extending the ModelSerializer class.
    '''
    class Meta:
        model = Well
        fields = ['id', 'bacia', 'estado', 'municipio', 'lat', 'long','formac']

class UserWellSerializer(serializers.ModelSerializer):
    '''
    Basic serializer class for the Well Model, extending the ModelSerializer class.
    '''
    class Meta:
        model = User_Well
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['id', 'bacia', 'estado', 'municipio', 'lat', 'long','formac','owner']
    