from relationship_app.models import Librarian, Library

# Example: Get a librarian who works in a specific library
librarian = Librarian.objects.get(library__name="Central Library")

print(librarian.name)
