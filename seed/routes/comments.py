"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from seed.routes.viewset import ViewSet

from app.models import Comment
from app.serializers import CommentSerializer

class CommentViewSet(
    ViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    def get_queryset(self):
        user = self.request.user
        return Comment.filter_permissions(
            super().get_queryset(), Comment.permission_filters(user))