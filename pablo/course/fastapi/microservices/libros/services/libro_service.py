from abc import ABC, abstractmethod
from typing import List


from pablo.course.fastapi.microservices.libros.schemes.libro_dto import LibroDto, LibroCreateDto


class LibroService(ABC):

    @abstractmethod
    def find_all(self) -> List[LibroDto]:
        ...

    @abstractmethod
    def find_by_id(self, libro_id: int) -> LibroDto | None:
        ...

    @abstractmethod
    def find_by_name(self, name: str) -> LibroDto | None:
        ...

    @abstractmethod
    def create(self, libro: LibroCreateDto) -> LibroDto:
        ...

    @abstractmethod
    def update(self, libro_id: int, libro: LibroCreateDto) -> LibroDto:
        ...

    @abstractmethod
    def delete(self, libro_id: int) -> bool:
        ...
