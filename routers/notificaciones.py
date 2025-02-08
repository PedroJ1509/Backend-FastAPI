from fastapi import APIRouter
from controllers.NotificacionesCotroller import enviar_notificacion

notificaciones = APIRouter()

@notificaciones.post("/enviar_notificacion/")
async def notificar(token: str, titulo: str, mensaje: str):
    """Endpoint para enviar una notificación push."""
    resultado = enviar_notificacion(token, titulo, mensaje)
    return resultado