**Purpose:** Show how you updated an existing `Book` record.

### ✅ Example content:
```markdown
# Update Operation

## Command:
```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
book
