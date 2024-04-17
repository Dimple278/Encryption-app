from django.db import models

class Message(models.Model):
    text = models.TextField()
    encrypted_text = models.TextField(blank=True, null=True)
