from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from fastapi import Request
from src.users import routers
from src.config import database


# Инициализация FastAPI
app = FastAPI()

# Инициализация базы данных
database.init_db()

# Подключение роутов
app.include_router(routers.router)

# Подключаем папку с HTML-шаблонами
templates = Jinja2Templates(directory="src/frontend/templates")

# Отдаём статические файлы (CSS, JS)
app.mount("/static", StaticFiles(directory="src/frontend/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
