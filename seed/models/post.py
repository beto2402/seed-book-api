"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.db import models
from seed.models.model import Model

class Post(Model):

    content = models.TextField(blank=True)
    picture = models.ForeignKey(
        'models.File', related_name='post_pictures',
        blank=False, null=False, on_delete=models.PROTECT)

    created_by = models.ForeignKey(
        'models.User', related_name='created_by_posts',
        blank=False, null=False, on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(
        'models.User', related_name='liked_by_posts', blank=False,
        db_table='_post__liked_by')

    class Meta:
        db_table = '_post'
        app_label = 'models'