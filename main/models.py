from django.db import models

class Conversation(models.Model):
    prompt = models.CharField(max_length=512)
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.prompt}: {self.response}"