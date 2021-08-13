from rest_framework import serializers

from .models import CustomUser, ProfileFeed


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True,
                                     'style': {'input_type': 'password'}}}

    def create(self, validated_data):
        """Create and return a new user"""
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

class ProfileFeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileFeed
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}