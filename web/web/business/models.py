from django.contrib.auth.models import AbstractUser
from django.db import models

class User(models.Model):
    fullname = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=255)

class CustomUser(AbstractUser):
    gender = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)


class Resim(models.Model):
    ad = models.CharField(max_length=100)
    resim = models.ImageField(upload_to='images/') 