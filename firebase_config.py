import firebase_admin
from firebase_admin import credentials, firestore

# Ruta al archivo JSON de credenciales descargado desde Firebase
cred = credentials.Certificate('./src/credentials.json')

# Inicializa la app de Firebase
firebase_admin.initialize_app(cred)

# Conecta a la base de datos Firestore
db = firestore.client()