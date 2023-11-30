from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Conversation
from django.contrib.auth import get_user_model



class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = '__all__'
        # fields = ['prompt', 'response']