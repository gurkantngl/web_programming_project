
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class Permission(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name


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

    roles = models.ManyToManyField(Role)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def has_permission(self, permission_name):
        for role in self.roles.all():
            if role.permissions.filter(name=permission_name).exists():
                return True
        return False

    def __str__(self):
        return self.fullname

