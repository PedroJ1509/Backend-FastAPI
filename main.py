from fastapi import FastAPI
from routers.product import router as product_router
from routers.articulo import articulo as articulo_router

app = FastAPI()


@app.get("/")
def message():
    return {"Hola mundo!!!"}


app.include_router(product_router)

app.include_router(articulo_router)