from rest_framework import serializers
from models.comment import Comment
from serializers.userSerializer import UserSerializer
from serializers.reviewSerializer import ReviewSerializer

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    review = ReviewSerializer(read_only = True)

    class Meta:
        model = Comment
        fields = '__all__'
