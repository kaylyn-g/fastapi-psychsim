

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
reviews: list[dict] = [
    {
        "id": 1,
        "author": "Alex R.",
        "star_rating": 5,
        "title": "BEST CAMERA OUT THERE TO DATE",
        "content": "Lorem ipsum dolor sit amet consectetur adipiscing elit Ut et massa mi. Aliquam in hendrerit urna. Pellentesque sit amet sapien fringilla, mattis ligula consectetur, ultrices mauris.",
        "date_posted": "12 January 2026"
    },
    {
        "id": 2,
        "author": "Jordan K.",
        "star_rating": 4.5,
        "title": "THE PIXEL QUALITY IS AMAZING",
        "content": "Lorem ipsum dolor sit amet consectetur adipiscing elit Ut et massa mi. Aliquam in hendrerit urna. Pellentesque sit amet sapien fringilla, mattis ligula consectetur, ultrices mauris.",
        "date_posted": "05 February 2026"
    },
]

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home():
    return {"message": "Hello World!"}

@app.get("/api/reviews/{id}", response_class=HTMLResponse)
async def get_reviews(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="reviews.html", context={"id": id}
    )