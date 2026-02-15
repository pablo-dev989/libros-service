import os
from fastapi import FastAPI

from pablo.course.fastapi.microservices.libros.config.db import engine, Base
from pablo.course.fastapi.microservices.libros.routers import libros
#import pablo.course.fastapi.microservices.libros.entities

app = FastAPI()

# Solo crea las tablas si la variable INIT_DB es "true"
if os.getenv("INIT_DB", "false").lower() == "true":
    print("LOG: Ejecutando creación de tablas...")
    Base.metadata.create_all(bind=engine)
else:
    print("LOG: Saltando creación de tablas (Modo producción)")

#Base.metadata.create_all(engine)
app.include_router(libros.router, prefix="/libros", tags=["libros"])