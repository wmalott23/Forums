from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=10),
    status = models.CharField(max_length=10),
    Icon = models.CharField(max_length=255)