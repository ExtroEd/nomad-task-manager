from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Строка подключения для SQLite
DATABASE_URL = "sqlite:///./test.db"  # Путь к базе данных SQLite

# Создаем соединение с базой данных SQLite (без необходимости в дополнительных параметрах)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Создаем SessionLocal для управления сессиями
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Основной базовый класс для моделей
Base = declarative_base()


# Функция для инициализации базы данных (создания таблиц)
def init_db():
    Base.metadata.create_all(bind=engine)
