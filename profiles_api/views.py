from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings


from .serializers import UserSerializer, ProfileFeedSerializer
from .models import CustomUser, ProfileFeed
from .permissions import IsProfileOwnerOrReadOnly, IsProfileFeedOwnerOrReadOnly


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


class UserLoginAPIView(ObtainAuthToken):
    """
    API endpoint for authenticating users with tokens.
    """
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileFeedViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows for creating, reading and updating profile feed items.
    """
    authentication_classes = (TokenAuthentication,)
    serializer_class = ProfileFeedSerializer
    queryset = ProfileFeed.objects.all()
    permission_classes = (IsProfileFeedOwnerOrReadOnly,
                          permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
