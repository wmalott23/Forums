from rest_framework import serializers
from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'topic', 'topic_id', 'title', 'image', 'user_info', 'user_info_id']
        depth = 1
    topic_id = serializers.IntegerField(write_only=True)
    user_info_id = serializers.IntegerField(write_only=True)