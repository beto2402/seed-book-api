"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

import graphene
from app.models import Comment
from app.models import User
from app.models import Post
from seed.schema.types import Comment as CommentType

class SaveCommentMutation(graphene.Mutation):
    
    comment = graphene.Field(CommentType)
    
    class Arguments:
        content = graphene.String(required=True)
        createdBy = graphene.Int(required=True)
        post = graphene.Int(required=False)

    def mutate(self, info, **kwargs):
        user = info.context.user
        comment = {}
        if "content" in kwargs: comment["content"] = kwargs["content"]
        if "createdBy" in kwargs:
            created_by = User.filter_permissions(
                User.objects, User.permission_filters(user))\
                .get(pk=kwargs["createdBy"])
            comment["created_by"] = created_by
        if "post" in kwargs:
            post = Post.filter_permissions(
                Post.objects, Post.permission_filters(user))\
                .get(pk=kwargs["post"])
            comment["post"] = post
        comment = Comment.objects.create(**comment)
        comment.save()
    
        return SaveCommentMutation(comment=comment)

class SetCommentMutation(graphene.Mutation):
    
    comment = graphene.Field(CommentType)
    
    class Arguments:
        id = graphene.Int(required=True)
        content = graphene.String(required=False)
        createdBy = graphene.Int(required=False)
        post = graphene.Int(required=False)

    def mutate(self, info, **kwargs):
        user = info.context.user
        comment = Comment.filter_permissions(
            Comment.objects, Comment.permission_filters(user))\
            .get(pk=kwargs["id"])
        if "content" in kwargs: comment.content = kwargs["content"]
        if "createdBy" in kwargs:
            created_by = User.objects.get(pk=kwargs["createdBy"])
            comment.created_by = created_by
        if "post" in kwargs:
            post = Post.objects.get(pk=kwargs["post"])
            comment.post = post
        comment.save()
    
        return SetCommentMutation(comment=comment)

class DeleteCommentMutation(graphene.Mutation):
    
    id = graphene.Int()
    
    class Arguments:
        id = graphene.Int(required=True)

    def mutate(self, info, **kwargs):
        comment_id = kwargs["id"]
        comment = Comment.objects.get(pk=kwargs["id"])
        comment.delete()
        return DeleteCommentMutation(id=comment_id)