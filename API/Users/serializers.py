from rest_framework import serializers
from Users.models import Poco_User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poco_User
        fields =["email",'username', 'password', 'profilepic']