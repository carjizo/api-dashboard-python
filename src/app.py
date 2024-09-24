from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from src.routes.user_info import user_info_router

app = FastAPI()
app.title = "Mi API InfoUsers"
app.version = "0.0.1"

app.include_router(user_info_router)


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')