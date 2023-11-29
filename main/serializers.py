from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Conversation
from django.contrib.auth import get_user_model

# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = get_user_model()
#         fields = ['username', 'email']

class ConversationSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Conversation
        fields = '__all__'