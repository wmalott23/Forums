from django.db import models
from comment.models import Comment
from emojis.models import Emojis
from user.models import User

# Create your models here.

class CommentEmoji(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    emoji = models.ForeignKey(Emojis, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)