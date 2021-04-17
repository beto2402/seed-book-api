"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import serializers
from app.models import Post
from app.models import User
from app.models import File
from seed.serializers.file import FileSerializer

class PostSerializer(serializers.ModelSerializer):
    
    picture = FileSerializer(read_only=True)

    created_by_id = serializers.PrimaryKeyRelatedField(
        source='created_by', queryset=User.objects.all(),
        required=True, allow_null=False)
    liked_by_ids = serializers.PrimaryKeyRelatedField(
        many=True, source='liked_by', queryset=User.objects.all(),
        required=True, allow_null=False)
    picture_id = serializers.PrimaryKeyRelatedField(
        source='picture', queryset=File.objects.all(),
        required=True, allow_null=False)

    class Meta:
        model = Post
        fields = (
            'id',
            'hash',
            'content',
            'picture',
            'picture_id',
            'created_by_id',
            'liked_by_ids',  
        )