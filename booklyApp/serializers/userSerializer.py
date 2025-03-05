from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
    
    def create(self, validated_data:dict):
        validated_data.pop('is_staff', False)
        return super().create(validated_data)
    