from django.shortcuts import render
from rest_framework import generics
from rest_framework import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

# List all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

# Retrieve book based on its ID
class BookDetailView(generics.RetrieveApiView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticatedOrReadOnly]

# Adding a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticated]

# Updating a book based on its ID
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.ojects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticated]

# Deleting a book based on its ID
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_class = [IsAuthenticated]


