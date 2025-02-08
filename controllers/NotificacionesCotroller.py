from firebase_config import db
from firebase_admin import  messaging

def enviar_notificacion(token: str, titulo: str, mensaje: str):
    """Envía una notificación push a un dispositivo específico."""
    try:
        mensaje_push = messaging.Message(
            notification=messaging.Notification(
                title=titulo,
                body=mensaje
            ),
            token=token  # Token del dispositivo móvil
        )
        response = messaging.send(mensaje_push)
        return {"success": True, "response": response}
    except Exception as e:
        return {"success": False, "error": str(e)}