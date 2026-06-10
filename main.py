from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="LibraryFlow")

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
def books(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="books.html"
    )