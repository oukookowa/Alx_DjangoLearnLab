from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
books = Book.objects.filter(author='author')

# List all books in a library
books = Book.objects.filter(library='library')

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library='library')