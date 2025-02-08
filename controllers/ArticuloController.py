from src.conexion_sqlserver import obtener_conexion
from models.articulo import Articulo

def obtener_articulos():
    conexion = obtener_conexion()
    if not conexion:
        return {"error": "No se pudo conectar a la base de datos"}
    
    cursor = conexion.cursor()
    cursor.execute("SELECT Articulo_ID,Articulo_CD, Articulo_Desc FROM Articulo where Articulo_Status=1 and Articulo_SiKit=1")
    articulos = cursor.fetchall()
    conexion.close()
    return [Articulo(Articulo_ID=a[0], Articulo_CD=a[1], Articulo_Desc=a[2], Costo=a[3]) for a in articulos]

def listar_articulos(id: int):
    print('este es el id:', id)
    conexion = obtener_conexion()
    if not conexion:
        return []
    
    cursor = conexion.cursor()
    cursor.execute("SELECT Articulo_ID,Articulo_CD, Articulo_Desc FROM Articulo where Articulo_ID = ?", (id,))
    articulo = cursor.fetchone()
    conexion.close()
    print(articulo)
    if articulo:
        return {"Articulo_ID": articulo[0], "Articulo_CD": articulo[1], "Articulo_Desc": articulo[2]}
    else:
        return {"error": "Artículo no encontrado"}
    
    