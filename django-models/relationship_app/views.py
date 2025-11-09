
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Check if user is a Librarian
def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'
a# django-models/relationship_app/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# --- Role check functions ---
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# --- Views ---
@user_passes_test(is_admin, login_url='/forbidden/')
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(is_librarian, login_url='/forbidden/')
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(is_member, login_url='/forbidden/')
def member_view(request):
    return render(request, 'member_view.html')

# Forbidden page
def forbidden_view(request):
    return render(request, 'forbidden.html')

# Librarian view
@user_passes_test(is_librarian, login_url='/forbidden/')
def librarian_view(request):
    return render(request, 'librarian_view.html')

# Forbidden page view
def forbidden_view(request):
    return render(request, 'forbidden.html')
