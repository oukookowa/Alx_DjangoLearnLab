from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

# Helper function to check user's role
def role_check(user, role):
    return user.is_authenticated and user.userprofile.role == role

# Admin view
@user_passes_test(lambda u: role_check(u, 'Admin'))
def admin_view(request):
    return render(request, 'admin_view.html')

# Librarian view
@user_passes_test(lambda u: role_check(u, 'Librarian'))
def librarian_view(request):
    return render(request, 'librarian_view.html')

# Member view
@user_passes_test(lambda u: role_check(u, 'Member'))
def member_view(request):
    return render(request, 'member_view.html')


# Create more views here.

class RegisterView(CreateView):
    form_class = UserCreationForm()
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

def list_books(request):
    books = Book.objects.all()
    context = {'list_books': books}
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'