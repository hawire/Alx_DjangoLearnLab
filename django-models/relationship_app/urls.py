
from django.urls import path
from .views import librarian_view, forbidden_view

urlpatterns = [
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('forbidden/', forbidden_view, name='forbidden'),
]
