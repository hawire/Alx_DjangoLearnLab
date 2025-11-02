from django.shortcuts import render
from .models import Book

# Example view to display all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})
