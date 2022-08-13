from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import App, Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "email"]


class AppSerializer(serializers.ModelSerializer):
    # owner_name = UserSerializer()
    owner_name = serializers.CharField(source='owner', read_only=True)

    class Meta:
        model = App
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
