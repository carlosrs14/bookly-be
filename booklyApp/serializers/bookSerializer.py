from rest_framework import serializers
from models import Book
from serializers.authorSerializer import AuthorSerializer
from serializers.genderSerializer import GenderSerializer

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True) 
    geners = GenderSerializer(many = True, read_only = True)
    
    class Meta:
        model = Book
        fields = '__all__'