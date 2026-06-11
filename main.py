from fastapi import FastAPI, Request, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from sqlalchemy.orm import Session

from app.database.connection import Base, engine, get_db
from app.models.book import Book
from app.services.book_service import list_books


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