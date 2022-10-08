from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    # reply_count = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('comment','author', 'post',)

    # def get_reply_count(self, obj):
    #     if obj.is_parent:
    #         return obj.children().count()
    #     return 0

    def get_author(self, obj):
        return obj.author