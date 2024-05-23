# business/models.py
from django.db import models

class User(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=255)
