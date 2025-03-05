from rest_framework import serializers
from models.favorite import Favorite
from serializers.reviewSerializer import ReviewSerializer
from serializers.userSerializer import UserSerializer

class FavoriteSerialzer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    review = ReviewSerializer(read_only = True)
    
    class Meta:
        model = Favorite
        fields = '__all__'
    