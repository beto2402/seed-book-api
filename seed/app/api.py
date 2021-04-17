"""
__Seed builder__v0.2.0
  AUTO_GENERATED (Read only)
  Modify via builder
"""

from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from app.routes import CommentViewSet
from app.routes import PostViewSet
from app.routes import UserViewSet
from app.routes import FileView

router = DefaultRouter()
router.register(r'comments', CommentViewSet)
router.register(r'posts', PostViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('files/', FileView.as_view()),
    url(r'^auth/', include('rest_auth.urls'))
]