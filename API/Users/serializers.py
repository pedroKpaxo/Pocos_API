from rest_framework import serializers


from rest_framework import serializers

from Users.models import CustomPocoUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomPocoUser
        fields = ['id', 'email', 'first_name', 'last_name']