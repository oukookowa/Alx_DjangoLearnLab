from django.urls import path
from . import views
from .views import LoginView, LogoutView, RegisterView

# Map views to url patterns
urlpatterns = [
    path('accounts/login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(template_name='blog/login.html'), name='logout'),
    path('accounts/register/', RegisterView.as_view(template_name='blog/register.html'), name='register'),
    path('accounts/profile/', views.profile_view, name='profile'),
]