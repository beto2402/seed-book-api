"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.contrib import admin
from djangoql.admin import DjangoQLSearchMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from app.models import Comment
from app.models import Post
from app.models import User
from app.models import File

class Admin:

    @staticmethod
    def register():
        
        class CommentResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = Comment
                fields = (
                    'id',
                    'created_at',
                    'content',
                    'created_by_id',
                    'post_id',
                )
        class CommentAdmin(ImportExportModelAdmin):
            resource_class = CommentResource
        
        class PostResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = Post
                fields = (
                    'id',
                    'created_at',
                    'content',
                    'picture',
                    'picture_id',
                    'created_by_id',
                    'liked_by_ids',
                )
        class PostAdmin(ImportExportModelAdmin):
            resource_class = PostResource
        
        class UserResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = User
                fields = (
                    'id',
                    'created_at',
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'is_active',
                    'profile_image',
                    'profile_image_id',
                )
        class UserAdmin(ImportExportModelAdmin):
            resource_class = UserResource
        
        class FileResource(DjangoQLSearchMixin, resources.ModelResource):
            class Meta:
                model = File
        class FileAdmin(ImportExportModelAdmin):
            resource_class = FileResource
        admin.site.register(Comment, CommentAdmin)
        admin.site.register(Post, PostAdmin)
        admin.site.register(User, UserAdmin)
        admin.site.register(File, FileAdmin)