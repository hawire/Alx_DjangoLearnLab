from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from .models import Book, Library, UserProfile   # include UserProfile for role checks

# -------------------------
# Function-based view: list all books
# -------------------------
@login_required
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# -------------------------
# Class-based view: library details
# -------------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["books"] = self.object.books.all()
        return context


# -------------------------
# Authentication Views
# -------------------------
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")  # redirect after login
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")


def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto-login after registration
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# -------------------------
# Librarian-only view
# -------------------------
@login_required
def librarian_dashboard(request):
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("You do not have a profile.")

    if profile.role == "Librarian":
        return render(request, "relationship_app/librarian_dashboard.html")
    else:
        return HttpResponseForbidden("Access denied. Only Librarians can view this page.")
