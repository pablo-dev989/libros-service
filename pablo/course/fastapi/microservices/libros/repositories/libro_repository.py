from abc import ABC, abstractmethod
from ast import List

from pablo.course.fastapi.microservices.libros.entities.libro import Libro


class LibroRepository(ABC):

    @abstractmethod
    def find_all(self) -> List[Libro]:
        ...

    @abstractmethod
    def find_by_id(self, libro_id: int) -> Libro | None:
        ...

    @abstractmethod
    def find_by_name(self, name: str) -> Libro | None:
        ...

    @abstractmethod
    def create(self, libro: Libro) -> Libro:
        ...

    @abstractmethod
    def remove(self, libro_id: int) -> bool:
        ...
