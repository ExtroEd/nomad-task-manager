from fastapi import FastAPI
from src.users import routers
from src.config import database


# Инициализация FastAPI
app = FastAPI()

# Инициализация базы данных
database.init_db()

# Подключение роутов
app.include_router(routers.router)
