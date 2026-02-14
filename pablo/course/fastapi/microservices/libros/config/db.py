from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from pablo.course.fastapi.microservices.libros.config.settings import settings

# 1. Definimos argumentos extra para SQLite
connect_args = {}
if settings.DATABASE_URI.startswith("sqlite"):
    connect_args = {"check_same_thread": False}

# 2. Creamos el engine manejando el pool_size
# SQLite no usa pool_size, así que lo pasamos solo si no es SQLite
engine_kwargs = {
    "echo": settings.SHOW_SQL,
    "connect_args": connect_args
}

if not settings.DATABASE_URI.startswith("sqlite"):
    engine_kwargs["pool_size"] = settings.POOL_SIZE

engine = create_engine(settings.DATABASE_URI, **engine_kwargs)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
