from sqlalchemy.orm import Session

from app.models.book import Book


def list_books(db: Session):
    return db.query(Book).all()


def create_book(db: Session, title: str, author: str, year: int, category: str, copies: int):
    book = Book(
        title=title,
        author=author,
        year=year,
        category=category,
        copies=copies,
        status="Disponível"
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    return book

def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()

    if book:
        db.delete(book)
        db.commit()

    return book