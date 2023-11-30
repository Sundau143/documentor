from django.db import models
from document.models import Document
from user.models import User


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

    document = models.ForeignKey(Document, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"Comment {self.id}"