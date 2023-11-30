from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_updated = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=20, default='Not provided', blank=True)
    role = models.CharField(max_length=55, default='Not provided', blank=True)
    total_document = models.IntegerField(default=0)


