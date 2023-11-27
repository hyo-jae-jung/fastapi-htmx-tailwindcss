import os

from fastapi import FastAPI, Request, Response
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

@app.get('/set-cookies')
async def set_cookie(response: Response):
    response.set_cookie(key="test",value="test111",httponly=True)
    return {
        "message": "쿠키가 생성됐습니다."
    }

@app.get("/get-cookies")
async def get_cookies(request: Request):
    # 클라이언트로부터 전송된 모든 쿠키 읽기
    cookies = request.cookies
    # 특정 쿠키의 값을 가져옵니다 (예: 'test' 쿠키)
    test_cookie = cookies.get("test", "쿠키가 없습니다")
    return templates.TemplateResponse("cookies.html",{
        "request":request,
        "cookies":cookies,
        "test_cookie": test_cookie
    })

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1", port=8000, reload=True)
    