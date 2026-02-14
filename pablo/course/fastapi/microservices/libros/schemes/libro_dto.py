from datetime import datetime
from pydantic import ConfigDict
from pablo.course.fastapi.microservices.libros.schemes.libro_create_dto import LibroCreateDto

class LibroDto(LibroCreateDto):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
