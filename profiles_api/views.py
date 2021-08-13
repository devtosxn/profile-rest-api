from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters

from .serializers import UserSerializer
from .models import CustomUser
from .permissions import IsProfileOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows for creating and update user profiles.
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsProfileOwnerOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
