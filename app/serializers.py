"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_comment_serializer():
    import seed.serializers.comment as SeedSerializer
    return SeedSerializer.CommentSerializer

def get_post_serializer():
    import seed.serializers.post as SeedSerializer
    return SeedSerializer.PostSerializer

def get_user_serializer():
    import seed.serializers.user as SeedSerializer
    return SeedSerializer.UserSerializer

def get_file_serializer():
    import seed.serializers.file as SeedSerializer
    return SeedSerializer.FileSerializer

CommentSerializer = get_comment_serializer()
PostSerializer = get_post_serializer()
UserSerializer = get_user_serializer()
FileSerializer = get_file_serializer()