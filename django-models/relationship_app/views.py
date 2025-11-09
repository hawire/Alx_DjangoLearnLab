
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Role check function
def is_librarian(user):
    """
    Returns True if the user is authenticated and has role 'Librarian'.
    """
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

# Librarian view
@user_passes_test(is_librarian, login_url='/forbidden/')
def librarian_view(request):
    """
    Only accessible to users with the 'Librarian' role.
    """
    return render(request, 'librarian_view.html')

# Optional: Forbidden access view
def forbidden_view(request):
    return render(request, 'forbidden.html')
