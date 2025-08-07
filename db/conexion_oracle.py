import oracledb as odb

def obtener_conexion():
    try:
        return odb.connect(
            user="C##libreria", 
            password="libreria", 
            dsn="localhost/xe")
    except odb.Error as ex:
        print("Error al conectar con la base de datos:",ex)
        return None