from rest_framework import serializers


from rest_framework import serializers

from Users.models import CustomPocoUser


class UserSerializer(serializers.ModelSerializer):
    '''
    Basic serializer class for the Custom User Model , extending the ModelSerializer class.
    '''

    class Meta:
        model = CustomPocoUser
        # - Add Fields
        fields = ['id', 'email','profilepic']