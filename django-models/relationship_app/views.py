
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Check if user is a Librarian
def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# Librarian view
@user_passes_test(is_librarian, login_url='/forbidden/')
def librarian_view(request):
    return render(request, 'librarian_view.html')

# Forbidden page view
def forbidden_view(request):
    return render(request, 'forbidden.html')
