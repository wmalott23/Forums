from django.db import models
from .models import Subject
from .models import User

# Create your models here.

class Thread(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=(100))
    description = models.CharField(max_length=(255))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    view = models.CharField(max_length=(30))
    timestamp = models.DateField()
