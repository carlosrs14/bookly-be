from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied
from ..serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.filter(id = self.request.user.id)
    
    def perform_destroy(self, instance:User):
        if self.request.user != instance:
            raise PermissionDenied("Not permissions.")
        instance.delete()
    
    def perform_update(self, serializer:UserSerializer):
        if self.request.user != serializer.instance:
            raise PermissionDenied("Not permissions.")
        serializer.save()
