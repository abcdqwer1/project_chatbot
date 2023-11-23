from django.db import models

class Message(models.Model):
    user = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Conversation(models.Model):
    prompt = models.CharField(max_length=512)
    response = models.TextField()

    def __str__(self):
        return f"{self.prompt}: {self.response}"