from db.conexion_oracle import obtener_conexion

def agregar_biblioteca(id_biblioteca, nombre_biblioteca, ubicacion_biblioteca):
    try:    
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO biblioteca VALUES(:1, :2, :3)",[id_biblioteca, nombre_biblioteca, ubicacion_biblioteca])
        conexion.commit()
    except Exception as ex:
        print("Error al insertar datos:",ex)
    finally:
        cursor.close()
        conexion.close()