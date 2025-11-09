from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# -------------------------
# Function-based view
# -------------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})


# -------------------------
# Class-based view
# -------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"

    # Optionally override get_context_data to add extra info
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add all books in this library
        context["books"] = self.object.books.all()
        return context
