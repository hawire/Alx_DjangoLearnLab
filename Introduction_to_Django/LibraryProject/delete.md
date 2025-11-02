**Purpose:** Show how you deleted the `Book` record and confirmed deletion.

### ✅ Example content:
```markdown
# Delete Operation

## Command:
```python
from bookshelf.models import Book

# Retrieve and delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
Book.objects.all()
