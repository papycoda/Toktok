#serializer for the user model

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'bio',
            'profile_pic',
            'created_at')
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    

