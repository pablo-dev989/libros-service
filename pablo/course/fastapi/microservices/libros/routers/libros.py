from typing import List

from fastapi import APIRouter, status, Depends, HTTPException

from pablo.course.fastapi.microservices.libros.dependencies.di import get_service
from pablo.course.fastapi.microservices.libros.schemes.libro_dto import LibroDto, LibroCreateDto
from pablo.course.fastapi.microservices.libros.services.libro_service import LibroService

router = APIRouter()

@router.get('/', response_model=List[LibroDto], status_code=status.HTTP_200_OK)
def list_libros(service: LibroService = Depends(get_service)) -> List[LibroDto]:
    return service.find_all()

@router.get('/{libro_id}', response_model=LibroDto, status_code=status.HTTP_200_OK)
def get_libro(libro_id: int, service: LibroService = Depends(get_service)) -> LibroDto | None:
    libro = service.find_by_id(libro_id)
    if not libro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Libro no encontrado')
    return libro

@router.get('/buscar/{name}', response_model=LibroDto, status_code=status.HTTP_200_OK)
def get_libro_by_name(name: str, service: LibroService = Depends(get_service)) -> LibroDto | None:
    libro = service.find_by_name(name)
    if not libro:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Libro: por nombre no encontrado')
    return libro

@router.post('/', response_model=LibroDto, status_code=status.HTTP_201_CREATED)
def create_libro(libro: LibroCreateDto, service: LibroService = Depends(get_service)):
    return service.create(libro)

@router.put('/{libro_id}', response_model=LibroDto, status_code=status.HTTP_202_ACCEPTED)
def update_libro(libro_id: int, libro: LibroCreateDto, service: LibroService = Depends(get_service)):
    return service.update(libro_id, libro)


