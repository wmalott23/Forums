from django.db import models
from .models import Thread
from .models import User

# Create your models here.

class Comment(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    timestamp = models.DateField()
    message = models.CharField(max_length=(255))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    