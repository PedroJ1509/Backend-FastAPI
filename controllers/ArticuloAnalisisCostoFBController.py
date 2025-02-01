from firebase_config import db
from fastapi import HTTPException

# Nombre de la colección
COLLECTION_NAME = "ArticuloAnalisisCosto"

# Crear un artículo
def create_analisis_costo(data):
    # Agregar un nuevo artículo en Firestore
    
    doc_ref = db.collection(COLLECTION_NAME).add(data)[1] 
    print(doc_ref)
    return  {"ArticuloAnalisisCosto_ID": doc_ref.id, **data}

# Leer un artículo por ID
async def get_analisis_costo(id: int):

    try :
        query = db.collection(COLLECTION_NAME).where("ArticuloAnalisisCosto_ID", "==", id).limit(1).stream()

        analisisCosto = None
        for doc in query:
            analisisCosto = doc.to_dict()
            analisisCosto["ArticuloAnalisisCosto_ID"] = doc.id  # Agregar ID del documento
        
        if not analisisCosto:
            raise HTTPException(status_code=404, detail=f"Registro no encontrado")

        return analisisCosto
    except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    

    # Obtener todos los artículos
def get_all_analisis_costo():
    docs = db.collection(COLLECTION_NAME).stream()
    return [doc.to_dict() for doc in docs]