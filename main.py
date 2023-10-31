from fastapi import FastAPI, Request
import uvicorn
# from router import router
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/')
async def index_test(request: Request):
    return templates.TemplateResponse("index.html",{
        "request":request,
    })

# app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1", port=8000, reload=True)
