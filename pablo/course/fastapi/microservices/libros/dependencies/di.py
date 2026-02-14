from fastapi import Depends
from sqlalchemy.orm import Session

from pablo.course.fastapi.microservices.libros.config.db import SessionLocal
from pablo.course.fastapi.microservices.libros.repositories.libro_repository_impl import LibroRepositoryImpl
from pablo.course.fastapi.microservices.libros.services.libro_service import LibroService
from pablo.course.fastapi.microservices.libros.services.libro_service_impl import LibroServiceImpl


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_service(db: Session = Depends(get_db)) -> LibroService:
    return LibroServiceImpl(LibroRepositoryImpl(db), db)
