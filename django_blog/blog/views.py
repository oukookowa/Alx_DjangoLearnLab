from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserProfileForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import UserProfile



# Register view for users to register and log them in after registeration
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

# User profile view for users to add bio, profile photo, etc.
@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user) # Get or create profile for logged in user

    if request.method('POST'):
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'blog/profile.html', {'form': form})

# Login view for users to login
class LoginView(LoginView):
    template_name = 'blog/login.html'
    success_url = reverse_lazy('index')

# Logout view for users to logout
class LogoutView(LogoutView):
    template_name = 'blog/logout.html'
    success_url = reverse_lazy('login')

