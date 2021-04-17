"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Comment(Model):

    content = models.CharField(max_length=155, blank=True)

    created_by = models.ForeignKey(
        'models.User', related_name='created_by_comments',
        blank=False, null=False, on_delete=models.CASCADE)
    post = models.ForeignKey(
        'models.Post', related_name='comments',
        blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = '_comment'
        app_label = 'models'