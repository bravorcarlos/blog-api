from rest_framework.routers import DefaultRouter
from .views import CommentAPIViewSet

router_comments = DefaultRouter()

router_comments.register(prefix='comments', basename='comments', viewset=CommentAPIViewSet)