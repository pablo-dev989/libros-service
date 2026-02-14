from pydantic import BaseModel

class LibroCreateDto(BaseModel):
    isbn: str
    name: str
    topic: str
    author: str
    year: int
    editorial: str