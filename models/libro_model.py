from db.conexion_oracle import obtener_conexion
from tkinter import messagebox
def agregar_libro(isbn, titulo_libro, autor_libro, year_publicacion, id_biblioteca):
    try:    
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO libro VALUES(:1, :2, :3, :4, :5)",[isbn, titulo_libro, autor_libro, year_publicacion, id_biblioteca])
        conexion.commit()
    except Exception as ex:
        print("Error al insertar datos:",ex)
    finally:
        cursor.close()
        conexion.close()
def obtener_bibliotecas():
    try:
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT id_biblioteca, nombre FROM biblioteca")
        bibliotecas = cursor.fetchall()
        biblioteca_dic = {nombre: id_biblioteca for id_biblioteca, nombre in bibliotecas}
        conexion.commit()
        return biblioteca_dic
    except Exception as ex:
        messagebox.showerror("ERROR!", "Ocurrio error al obtener bibliotecas: ", ex)
    finally:
        cursor.close()
        conexion.close()