from rest_framework import serializers
from models.like import Like
from serializers.userSerializer import UserSerializer
from serializers.reviewSerializer import ReviewSerializer

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    review =ReviewSerializer(read_only = True)

    class Meta:
        model = Like
        fields = '__all__'
        