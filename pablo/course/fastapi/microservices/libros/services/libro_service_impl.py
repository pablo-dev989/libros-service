from typing import List

from sqlalchemy.orm import Session

from pablo.course.fastapi.microservices.libros.entities.libro import Libro
from pablo.course.fastapi.microservices.libros.repositories.libro_repository import LibroRepository
from pablo.course.fastapi.microservices.libros.schemes.libro_dto import LibroDto, LibroCreateDto
from pablo.course.fastapi.microservices.libros.services.libro_service import LibroService


class LibroServiceImpl(LibroService):
    def __init__(self, repo: LibroRepository, db: Session):
        self._repo = repo
        self._db = db

    def find_all(self) -> List[LibroDto]:
        return [LibroDto.model_validate(entity) for entity in self._repo.find_all()]

    def find_by_id(self, libro_id: int) -> LibroDto | None:
        libro_entity = self._repo.find_by_id(libro_id)
        if libro_entity:
            return LibroDto.model_validate(libro_entity)
        return None

    def find_by_name(self, name: str) -> LibroDto | None:
        libro_entity = self._repo.find_by_name(name)
        if libro_entity:
            return LibroDto.model_validate(libro_entity)
        return None

    def create(self, libro: LibroCreateDto) -> LibroDto:
        libro_entity = Libro(isbn=libro.isbn,
                             name=libro.name,
                             topic=libro.topic,
                             author=libro.author,
                             year=libro.year,
                             editorial=libro.editorial)
        try:
            self._db.add(libro_entity)
            self._db.commit()
            self._db.refresh(libro_entity)
            return LibroDto.model_validate(libro_entity)
        except Exception:
            self._db.rollback()
            raise

    def update(self, libro_id: int, libro: LibroCreateDto) -> LibroDto | None:
        libro_entity = self._repo.find_by_id(libro_id)
        if not libro_entity:
            return None
        libro_entity.isbn = libro.isbn
        libro_entity.name = libro.name
        libro_entity.topic = libro.topic
        libro_entity.author = libro.author
        libro_entity.year = libro.year
        libro_entity.editorial = libro.editorial
        try:
            self._db.add(libro_entity)
            self._db.commit()
            self._db.refresh(libro_entity)
            return LibroDto.model_validate(libro_entity)
        except Exception:
            self._db.rollback()
            raise


    def delete(self, libro_id: int) -> bool:
        libro_entity = self._repo.find_by_id(libro_id)
        if not libro_entity:
            return False
        try:
            self._db.delete(libro_entity)
            self._db.commit()
            return True
        except Exception:
            self._db.rollback()
            raise