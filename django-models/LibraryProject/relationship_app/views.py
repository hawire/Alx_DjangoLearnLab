from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library

# -------------------------
# Function-based view
# -------------------------
def list_books(request):
    books = Book.objects.all()
    # Explicitly reference relationship_app/list_books.html
    return render(request, "relationship_app/list_books.html", {"books": books})


# -------------------------
# Class-based view
# -------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # also explicit path
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context
