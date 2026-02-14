from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from pablo.course.fastapi.microservices.libros.config.db import Base


class Libro(Base):
    __tablename__ = "libros"

    id: Mapped[int] = mapped_column(Integer,primary_key=True, autoincrement=True)
    isbn: Mapped[str] = mapped_column(String(20),nullable=False, index=True)
    name: Mapped[str] = mapped_column(String(256), nullable=False, index=True, unique=True)
    topic: Mapped[str] = mapped_column(String(512), nullable=False)
    author: Mapped[str] = mapped_column(String(512), nullable=False, index=True)
    year: Mapped[int] = mapped_column(Integer,nullable=False, index=True)
    editorial: Mapped[str] = mapped_column(String(256), nullable=False, index=True)
    created_at: Mapped[str] = mapped_column(DateTime, server_default=func.now())