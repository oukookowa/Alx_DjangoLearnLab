from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    context = {'books_list': books}
    return render(request, 'relationship_app/book_list.html', context)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'