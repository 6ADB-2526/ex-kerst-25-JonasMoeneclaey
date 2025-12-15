from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField(max_length=25)
    password = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    role = models.CharField(max_length=20)
    isSuperuser = models.BooleanField()