from django.db import models

# Create your models here.

class Topic(models.Model):
    Title = models.CharField(max_length=100)