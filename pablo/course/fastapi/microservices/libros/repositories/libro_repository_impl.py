from ast import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from pablo.course.fastapi.microservices.libros.entities.libro import Libro
from pablo.course.fastapi.microservices.libros.repositories.libro_repository import LibroRepository


class LibroRepositoryImpl(LibroRepository):

    def __init__(self, db: Session):
        self._db = db

    def find_all(self) -> List[Libro]:
        return list(self._db.scalars(select(Libro).order_by(Libro.id.asc())).all())

    def find_by_id(self, libro_id: int) -> Libro | None:
        return self._db.get(Libro, libro_id)

    def find_by_name(self, name: str) -> Libro | None:
        # .ilike permite que "Libro" sea igual a "libro"
        stmt = select(Libro).where(Libro.name.ilike(name))
        return self._db.execute(stmt).scalar_one_or_none()

    def create(self, libro: Libro) -> Libro:
        self._db.add(libro)
        return libro

    def remove(self, libro_id: int) -> bool:
        libro = self._db.get(Libro, libro_id)
        if libro:
            self._db.delete(libro)
            self._db.commit()
            return True
        return False
