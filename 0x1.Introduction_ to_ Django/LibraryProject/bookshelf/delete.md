# Code deletes the book object associated with id=1
book = Book.objects.get(id=1)
book.delete()