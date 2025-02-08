from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from controllers.ArticuloFBController import create_articulo, get_articulo, get_all_articulos, incrementar_precios_articulos
from models.articulo import Articulo
from models.incrementoPrecioRequest import IncrementoPrecioRequest

articuloFB = APIRouter()

# Endpoint para crear un artículo
@articuloFB.post("/articulosFB/")
async def crear_articulo(articulo: Articulo):
    data = articulo.dict()
    return create_articulo(data)

# Endpoint para obtener un artículo por ID
@articuloFB.get("/articulosFB/{articulo_id}")
async def obtener_articulo(articulo_id: int):
    return await get_articulo(articulo_id)

# Endpoint para obtener todos los artículos
@articuloFB.get("/articulosFB/")
async def obtener_todos_los_articulos():
    return get_all_articulos()

#Endpoint para aumentar precio a los articulos
@articuloFB.post("/incrementarPrecio")
async def incrementarPrecioArticulos(request: IncrementoPrecioRequest):
    return await incrementar_precios_articulos(request)