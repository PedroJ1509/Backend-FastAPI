from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from controllers.ArticuloAnalisisCostoFBController import create_analisis_costo, get_analisis_costo, get_all_analisis_costo
from models.articuloAnalisisCosto import ArticuloAnalisisCosto

articuloAnalisisCostoFB = APIRouter()

# Endpoint para crear un artículo
@articuloAnalisisCostoFB.post("/articuloAnalisisCostoFB/")
async def crear_analisis_costo(articulo: ArticuloAnalisisCosto):
    data = articulo.dict()
    return create_analisis_costo(data)

# Endpoint para obtener un artículo por ID
@articuloAnalisisCostoFB.get("/articuloAnalisisCostoFB/{articuloAnalisisCosto_id}")
async def obtener_analisis_costo(articuloAnalisisCosto_id: int):
    return await get_analisis_costo(articuloAnalisisCosto_id)

# Endpoint para obtener todos los artículos
@articuloAnalisisCostoFB.get("/articuloAnalisisCostoFB/")
async def obtener_todos_los_analisis_costo():
    return get_all_analisis_costo()