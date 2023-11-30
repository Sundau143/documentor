from django.db import models
from user.models import User
from tinymce import models as tinymce_models

class Document(models.Model):
    name = models.CharField(max_length=255)
    content = tinymce_models.HTMLField(default="# Введіть вміст документа у вигляді Markdown")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    group = models.TextField(default="Not provided")
    users = models.ManyToManyField(User)
