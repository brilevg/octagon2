from .models import Book
from .models import Category


def create_category(session, title):
    category = Category(title=title)

    session.add(category)

    session.commit()

    session.refresh(category)

    return category


def get_categories(session):
    return session.query(Category).all()


def update_category(session, category_id, new_title):
    category = session.get(Category, category_id)

    if category:
        category.title = new_title
        session.commit()

    return category


def delete_category(session, category_id):
    category = session.get(Category, category_id)

    if category:
        session.delete(category)
        session.commit()



def create_book(session, title, description, price, url, category):
    book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category=category,
    )

    session.add(book)

    session.commit()

    session.refresh(book)

    return book


def get_books(session):
    return session.query(Book).all()


def update_book(session, book_id, new_price):
    book = session.get(Book, book_id)

    if book:
        book.price = new_price
        session.commit()

    return book


def delete_book(session, book_id):
    book = session.get(Book, book_id)

    if book:
        session.delete(book)
        session.commit()