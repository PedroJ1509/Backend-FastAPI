from typing import List
from fastapi import APIRouter
from models.articulo import Articulo
from controllers.ArticuloController import obtener_articulos, listar_articulos

articulo = APIRouter()

@articulo.get("/articulos/")
def get_articulos():
    return obtener_articulos()

@articulo.get("/articulos/{id}")
def get_articulo(id: int):
    print(id)
    return listar_articulos(id)