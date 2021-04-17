"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Post
from app.models import User
from app.models import File
from seed.schema.types import Post as PostType

class SavePostMutation(graphene.Mutation):
    
    post = graphene.Field(PostType)
    
    class Arguments:
        content = graphene.String(required=True)
        picture = graphene.Int(required=True)
        createdBy = graphene.Int(required=True)
        likedBy = graphene.List(graphene.Int)

    def mutate(self, info, **kwargs):
        user = info.context.user
        post = {}
        if "content" in kwargs: post["content"] = kwargs["content"]
        if "picture" in kwargs:
            picture = File.filter_permissions(
                File.objects, File.permission_filters(user))\
                .get(pk=kwargs["picture"])
            post["picture"] = picture
        if "createdBy" in kwargs:
            created_by = User.filter_permissions(
                User.objects, User.permission_filters(user))\
                .get(pk=kwargs["createdBy"])
            post["created_by"] = created_by
        post = Post.objects.create(**post)
        if "likedBy" in kwargs:
            post.liked_by.clear()
            for liked_by_id in kwargs["likedBy"]:
                liked_by = User.filter_permissions(
                    User.objects, User.permission_filters(user))\
                    .get(pk=liked_by_id)
                post.liked_by.add(liked_by)
        post.save()
    
        return SavePostMutation(post=post)

class SetPostMutation(graphene.Mutation):
    
    post = graphene.Field(PostType)
    
    class Arguments:
        id = graphene.Int(required=True)
        content = graphene.String(required=False)
        picture = graphene.Int(required=False)
        createdBy = graphene.Int(required=False)
        likedBy = graphene.List(graphene.Int)

    def mutate(self, info, **kwargs):
        user = info.context.user
        post = Post.filter_permissions(
            Post.objects, Post.permission_filters(user))\
            .get(pk=kwargs["id"])
        if "content" in kwargs: post.content = kwargs["content"]
        if "picture" in kwargs:
            picture = File.objects.get(pk=kwargs["picture"])
            post.picture = picture
        if "createdBy" in kwargs:
            created_by = User.objects.get(pk=kwargs["createdBy"])
            post.created_by = created_by
        if "likedBy" in kwargs:
            post.liked_by.clear()
            for liked_by_id in kwargs["likedBy"]:
                liked_by = User.objects.get(pk=liked_by_id)
                post.liked_by.add(liked_by)
        post.save()
    
        return SetPostMutation(post=post)

class DeletePostMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        post_id = kwargs["id"]
        post = Post.objects.get(pk=kwargs["id"])
        post.delete()
        return DeletePostMutation(id=post_id)