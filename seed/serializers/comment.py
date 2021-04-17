"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Comment
from app.models import User
from app.models import Post

class CommentSerializer(serializers.ModelSerializer):

    created_by_id = serializers.PrimaryKeyRelatedField(
        source='created_by', queryset=User.objects.all(),
        required=True, allow_null=False)
    post_id = serializers.PrimaryKeyRelatedField(
        source='post', queryset=Post.objects.all(),
        required=False, allow_null=True)

    class Meta:
        model = Comment
        fields = (
            'id',
            'hash',
            'content',
            'created_by_id',
            'post_id',  
        )