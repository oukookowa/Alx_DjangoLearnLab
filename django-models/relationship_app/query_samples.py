from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
books = Book.objects.filter(author='author')

# List all books in a library
library = Library.objects.get(name=library_name)
books = Book.objects.all()

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library='library')