from django.urls import path
from . import views
from .views import LoginView, LogoutView, RegisterView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, IndexView

# Map blog views to url patterns
urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('home/', IndexView.as_view(), name='index'),  # Index page
    path('posts/', PostListView.as_view(), name='post_list'),  # List all posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Post details
    path('post/new/', PostCreateView.as_view(), name='post_create'),  # Create a new post
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),  # Edit/update a post
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Delete a post

]