"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_comment_viewset():
    import seed.routes.comments as SeedViewSet
    return SeedViewSet.CommentViewSet

def get_post_viewset():
    import seed.routes.posts as SeedViewSet
    return SeedViewSet.PostViewSet

def get_user_viewset():
    import seed.routes.users as SeedViewSet
    return SeedViewSet.UserViewSet

def get_file_view():
    import seed.routes.files as SeedView
    return SeedView.FileView

CommentViewSet = get_comment_viewset()
PostViewSet = get_post_viewset()
UserViewSet = get_user_viewset()
FileView = get_file_view()