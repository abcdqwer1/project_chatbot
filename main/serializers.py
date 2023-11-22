from rest_framework.serializers import ModelSerializer
from .models import Message
from django.contrib.auth import get_user_model


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class MessageSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Message
        fields = [
            'id',
            'user',
            'content',
            'created_at',
            'updated_at',
        ]