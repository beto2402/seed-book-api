"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

def get_comment():
    import seed.models.comment as SeedModel
    return SeedModel.Comment

def get_post():
    import seed.models.post as SeedModel
    return SeedModel.Post

def get_user():
    import seed.models.user as SeedModel
    return SeedModel.User

def get_file():
    import seed.models.file as SeedFile
    return SeedFile.File

Comment = get_comment()
Post = get_post()
User = get_user()
File = get_file()