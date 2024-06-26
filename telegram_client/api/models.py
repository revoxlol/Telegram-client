from django.db import models

class Message(models.Model):
    chat_id = models.BigIntegerField()
    username = models.CharField(max_length=255)
    is_self = models.BooleanField()
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['chat_id', 'timestamp']),
        ]
