from fastapi import FastAPI
from routers.product import router as product_router
from routers.articulo import articulo as articulo_router
from routers.articuloFB import articuloFB as articuloFB_router
from routers.articuloAnalisisCostoFB import articuloAnalisisCostoFB as articuloAnalisisCostoFB_router
from routers.notificaciones import notificaciones as notificaciones_router

app = FastAPI()


@app.get("/")
def message():
    return {"Hola mundo!!!"}

app.include_router(product_router)

app.include_router(articulo_router)
app.include_router(articuloFB_router)
app.include_router(articuloAnalisisCostoFB_router)
app.include_router(notificaciones_router)