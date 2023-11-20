import os

from fastapi import FastAPI, Request
from routes.users import user_router
from routes.events import event_router

import uvicorn

from database.connection import Settings

from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.realpath("__file__"))

settings = Settings()
app.include_router(user_router,prefix="/user")
app.include_router(event_router,prefix="/event")

templates = Jinja2Templates(directory="templates")
templates.env.globals["STATIC_URL"] = "/static"

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

@app.on_event("startup")
async def init_db():
    await settings.initialize_database()

@app.get('/')
async def index_test(request: Request):
    return templates.TemplateResponse("index.html",{
        "request":request,
        "BASE_DIR":BASE_DIR,
    })

@app.get('/example')
async def contact_test(request: Request):
    return templates.TemplateResponse("contact.html",{
        "request":request,
        "BASE_DIR":BASE_DIR,
    })


if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1", port=8000, reload=True)
    