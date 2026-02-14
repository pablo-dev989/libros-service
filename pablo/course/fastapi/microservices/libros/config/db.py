from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from pablo.course.fastapi.microservices.libros.config.settings import settings

engine = create_engine(settings.DATABASE_URI, echo=settings.SHOW_SQL, pool_size=settings.POOL_SIZE)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()
