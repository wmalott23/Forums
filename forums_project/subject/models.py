from django.db import models
from topic.models import Topic
from user.models import UserInfo

# Create your models here.

class Subject(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    title = models.CharField(max_length=(30))
    description = models.CharField(max_length=(255))
    image = models.CharField(max_length=(255))
    user_info = models.ForeignKey(UserInfo, on_delete=models.CASCADE)