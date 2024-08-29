from django.urls import path, include
from .views import BookViewSet  # Import the view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet)
urlpatterns = [
    #path('books/', BookList.as_view(), name='book-list'),  # Define the URL pattern for the view
    path('api/', include(router.urls)),
]
