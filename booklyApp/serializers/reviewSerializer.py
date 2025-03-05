from rest_framework import serializers
from models.review import Review
from serializers.userSerializer import UserSerializer
from serializers.bookSerializer import BookSerializer

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    book = BookSerializer(read_only = True)
    
    class Meta:
        model = Review
        fields = '__all__'