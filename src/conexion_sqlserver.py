import pyodbc

def obtener_conexion():
    try:
        conexion = pyodbc.connect(
            'DRIVER={SQL Server};SERVER=DESKTOP-NCKVQ6L\MSSQLSERVER2019;DATABASE=GestionEmpOld;UID=sa;PWD=PedroJ85'
        )
        return conexion
    except Exception as e:
        print("Error en la conexión:", e)
        return None
