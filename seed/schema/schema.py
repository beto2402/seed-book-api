"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""
import graphene

import seed.schema.types
import seed.mutations.comment
import seed.mutations.post
import seed.mutations.user

class Query(seed.schema.types.Query, graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    
    saveComment = seed.mutations.comment.SaveCommentMutation.Field()
    setComment = seed.mutations.comment.SetCommentMutation.Field()
    deleteComment = seed.mutations.comment.DeleteCommentMutation.Field()
    savePost = seed.mutations.post.SavePostMutation.Field()
    setPost = seed.mutations.post.SetPostMutation.Field()
    deletePost = seed.mutations.post.DeletePostMutation.Field()
    saveUser = seed.mutations.user.SaveUserMutation.Field()
    setUser = seed.mutations.user.SetUserMutation.Field()
    deleteUser = seed.mutations.user.DeleteUserMutation.Field()
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)