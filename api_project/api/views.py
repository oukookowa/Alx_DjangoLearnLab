from rest_framework import viewsets #generics
from .models import Book  # Import your Book model
from .serializers import BookSerializer  # Import the serializer you just created

#class BookList(generics.ListAPIView):
    #queryset = Book.objects.all()  # Define the queryset to return all Book instances
    #serializer_class = BookSerializer  # Use the BookSerializer to serialize the data

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer