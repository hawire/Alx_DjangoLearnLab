from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    def setUp(self):
        self.book = Book.objects.create(
            title="1984",
            author="George Orwell",
            publication_year=1949
        )

    def test_book_creation(self):
        self.assertEqual(self.book.title, "1984")
        self.assertEqual(self.book.author, "George Orwell")
        self.assertEqual(self.book.publication_year, 1949)

    def test_book_str(self):
        self.assertEqual(str(self.book), "1984")
