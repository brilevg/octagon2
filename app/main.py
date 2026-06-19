from db.db import SessionLocal

from db.crud import get_categories
from db.crud import get_books

session = SessionLocal()

print("Categories:")

for category in get_categories(session):
    print(category.id, category.title)

print()

print("Books:")

for book in get_books(session):
    print(
        book.id,
        book.title,
        book.price,
        book.category.title
    )

session.close()