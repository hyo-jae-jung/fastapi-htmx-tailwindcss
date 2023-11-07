import os

from fastapi import FastAPI, Request
import uvicorn
# from router import router
from fastapi.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles

BASE_DIR = os.path.dirname(os.path.realpath("__file__"))

app = FastAPI()
templates = Jinja2Templates(directory="templates")
templates.env.globals["STATIC_URL"] = "/static"

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

@app.get('/')
async def index_test(request: Request):
    return templates.TemplateResponse("index.html",{
        "request":request,
        "BASE_DIR":BASE_DIR,
    })

@app.get('/contact')
async def contact_test(request: Request):
    return templates.TemplateResponse("contact.html",{
        "request":request,
        "BASE_DIR":BASE_DIR,
    })

# app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1", port=8000, reload=True)
    