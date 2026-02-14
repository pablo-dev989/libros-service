from fastapi import FastAPI

from pablo.course.fastapi.microservices.libros.config.db import engine, Base
from pablo.course.fastapi.microservices.libros.routers import libros
import pablo.course.fastapi.microservices.libros.entities

app = FastAPI()
Base.metadata.create_all(engine)
app.include_router(libros.router, prefix="/libros", tags=["libros"])