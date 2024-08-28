from rest_framework import generics
from .models import Book  # Import your Book model
from .serializers import BookSerializer  # Import the serializer you just created

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Define the queryset to return all Book instances
    serializer_class = BookSerializer  # Use the BookSerializer to serialize the data
