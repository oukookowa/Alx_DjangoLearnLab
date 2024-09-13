from django.urls import path
from . import views
from .views import LoginView, LogoutView, RegisterView, IndexView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import CommentListView, CommentDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView, 

# Map blog views to url patterns
urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('home/', IndexView.as_view(), name='index'),  # Index page
    path('posts/', PostListView.as_view(), name='post_list'),  # List all posts
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),  # Post details
    path('posts/new/', PostCreateView.as_view(), name='post_create'),  # Create a new post
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),  # Edit/update a post
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),  # Delete a post
    path('posts/<int:pk>/comments/', CommentListView.as_view(), name='comment_list'),  # List all coments of a post
    path('posts/<int:pk>/comments/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),  # Comment details
    path('posts/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),  # Create a new comment on a post
    path('posts/<int:pk>/comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),  # Edit/update a comment on a post
    path('posts/<int:pk>/comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),  # Delete a comment on a post

]