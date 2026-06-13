from fastapi import FastAPI, Request, Depends, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from app.database.connection import Base, engine, get_db
from app.models.book import Book
from app.services.book_service import list_books, create_book, delete_book, update_book


app = FastAPI(title="LibraryFlow")

Base.metadata.create_all(bind=engine)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def login(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )


@app.get("/dashboard")
def dashboard(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="dashboard.html"
    )


@app.get("/books")
def books(request: Request, db: Session = Depends(get_db)):
    books_list = list_books(db)

    return templates.TemplateResponse(
        request=request,
        name="books.html",
        context={"books": books_list}
    )

@app.post("/books")
def create_book_route(
    title: str = Form(...),
    author: str = Form(...),
    year: int = Form(...),
    category: str = Form(...),
    copies: int = Form(...),
    db: Session = Depends(get_db)
):
    create_book(
        db=db,
        title=title,
        author=author,
        year=year,
        category=category,
        copies=copies
    )

    return RedirectResponse(
        url="/books",
        status_code=303
    )

@app.post("/books/{book_id}/delete")
def delete_book_route(book_id: int, db: Session = Depends(get_db)):
    delete_book(db, book_id)

    return RedirectResponse(
    url="/books?deleted=1",
    status_code=303
)

@app.post("/books/{book_id}/edit")
def update_book_route(
    book_id: int,
    title: str = Form(...),
    author: str = Form(...),
    year: int = Form(...),
    category: str = Form(...),
    copies: int = Form(...),
    db: Session = Depends(get_db)
):
    update_book(
        db=db,
        book_id=book_id,
        title=title,
        author=author,
        year=year,
        category=category,
        copies=copies
    )

    return RedirectResponse(
        url="/books?updated=1",
        status_code=303
    )

@app.get("/loans")
def loans(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="loans.html"
    )


@app.get("/users")
def users(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="users.html"
    )