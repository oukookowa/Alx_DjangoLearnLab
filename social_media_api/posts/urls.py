from django.urls import path, include
from .views import PostViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter

# Create a router to register the viewsets
router = DefaultRouter()
router.register(r'posts', PostViewSet) # Registers postviewset
router.register(r'comments', CommentViewSet) # Registers commentviewset


# API urls are generated automatically by the router
urlpatterns = [
    path('',include(router.urls)),
]