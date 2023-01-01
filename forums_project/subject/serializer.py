from rest_framework import serializers
from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject,
        fields = ['id', 'topic', 'topic_id', 'title', 'image', 'user'],
        depth = 1
    topic_id = serializers.IntegerField(write_only=True)