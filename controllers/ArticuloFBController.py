from firebase_config import db
from fastapi import HTTPException
from firebase_admin import firestore, messaging
import asyncio

db = firestore.client()
# Nombre de la colección
COLLECTION_NAME = "ArticuloCosto"

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

# Crear un artículo
async def incrementar_precios_articulos(data):
    # Agregar un nuevo artículo en Firestore
    
    docs = db.collection(COLLECTION_NAME).stream()
    tareas = [actualizar_precio_producto(doc.reference, data.porcentaje) for doc in docs]

    # Ejecutar las actualizaciones en paralelo
    resultados = await asyncio.gather(*tareas)

     # Enviar la notificación en segundo plano usando el token del cliente
    #asyncio.create_task(enviar_notificacion_fcm(f"Precios incrementados en un {data.porcentaje}%", data.tokenFirebase))

    
    return {"mensaje": "Proceso completado", "detalles": []}

async def actualizar_precio_producto(doc_ref, porcentaje):
    """ Actualiza el precio de un producto en Firestore """
    try:
        doc = doc_ref.get()
        if doc.exists:
            data = doc.to_dict()
            nuevo_precio = round(data.get("Costo", 0) * (1 + porcentaje / 100), 2)
            doc_ref.update({"Costo": nuevo_precio})
            return f"Producto {doc_ref.id} actualizado a {nuevo_precio}"
    except Exception as e:
        return f"Error actualizando {doc_ref.id}: {str(e)}"
    
async def enviar_notificacion_fcm(mensaje,token_fcm):
    """ Enviar notificación a los dispositivos usando Firebase Cloud Messaging """
    try:
        message = messaging.Message(
            notification=messaging.Notification(
                title="Actualización de Precios",
                body=mensaje
            ),
            token=token_fcm  # Enviar al token específico
        )
        response = messaging.send(message)
        print("Notificación enviada:", response)
    except Exception as e:
        print("Error enviando notificación:", str(e))