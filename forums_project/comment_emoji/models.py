from django.db import models
from .models import Comment
from .models import Emoji
from .models import User

# Create your models here.

class CommentEmoji(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    emoji = models.ForeignKey(Emoji, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)