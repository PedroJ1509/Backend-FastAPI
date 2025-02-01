from firebase_config import db
from fastapi import HTTPException

# Nombre de la colección
COLLECTION_NAME = "articulo"

# Crear un artículo
def create_articulo(data):
    # Agregar un nuevo artículo en Firestore
    
    doc_ref = db.collection(COLLECTION_NAME).add(data)[1] 
    print(doc_ref)
    return  {"Articulo_Id": doc_ref.id, **data}

# Leer un artículo por ID
async def get_articulo(id: int):

    try :
        query = db.collection(COLLECTION_NAME).where("Articulo_ID", "==", id).limit(1).stream()

        articulo = None
        for doc in query:
            articulo = doc.to_dict()
            articulo["Articulo_Id"] = doc.id  # Agregar ID del documento
        
        if not articulo:
            raise HTTPException(status_code=404, detail=f"Artículo con Articulo_ID = {id} no encontrado")

        return articulo
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    

    # Obtener todos los artículos
def get_all_articulos():
    docs = db.collection(COLLECTION_NAME).stream()
    return [doc.to_dict() for doc in docs]