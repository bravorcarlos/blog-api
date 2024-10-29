from rest_framework.routers import DefaultRouter
from .views import CategoryAPIViewSet

router_categories = DefaultRouter()

router_categories.register(prefix='categories', basename='categories', viewset=CategoryAPIViewSet)
