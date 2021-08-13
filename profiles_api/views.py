from rest_framework import viewsets

from .serializers import UserSerializer
from .models import CustomUser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows for creating and update user profiles.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
