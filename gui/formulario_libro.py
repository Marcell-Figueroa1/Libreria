import tkinter as tk
from models.libro_model import agregar_libro, obtener_bibliotecas
from tkinter import messagebox

def crear_libro():
    ventana = tk.Toplevel()
    ventana.title("Formulario libro")
    # Dimensiones de la ventana
    alturaV = 300
    anchoV = 450
    # Dimensiones de la pantalla
    AlturaPantalla = ventana.winfo_screenheight()
    AnchoPantalla = ventana.winfo_screenwidth()
    # Calcular posición x, y para centrar
    x = (AnchoPantalla - anchoV) // 2
    y = (AlturaPantalla - alturaV) // 2
    # Posición de la ventana en pantalla (Centro)
    ventana.geometry(f"{anchoV}x{alturaV}+{x}+{y}")
    # Label y input del ISBN del libro
    tk.Label(ventana,text="ISBN del libro: ").grid(row=0, column=0, sticky="e")
    input_ISBN = tk.Entry(ventana)
    input_ISBN.grid(row=0, column=1, padx=5, pady=5, sticky="e")
    # Label y input del titulo del libro
    tk.Label(ventana,text="Titulo del libro: ").grid(row=1, column=0, sticky="e")
    input_Titulo = tk.Entry(ventana)
    input_Titulo.grid(row=1, column=1, padx=5, pady=5, sticky="e")
    # Label y input del autor del libro
    tk.Label(ventana,text="Autor del libro: ").grid(row=2, column=0, sticky="e")
    input_autor = tk.Entry(ventana)
    input_autor.grid(row=2, column=1, padx=5, pady=5, sticky="e")
    # Label y input del año de publicación
    tk.Label(ventana,text="Año de publicación del libro ej(2000): ").grid(row=3, column=0, sticky="e")
    input_yearP = tk.Entry(ventana)
    input_yearP.grid(row=3, column=1, padx=5, pady=5, sticky="e")
    # Menu de selección de las bibliotecas
    tk.Label(ventana, text="Seleccione una biblioteca: ").grid(row=4, column=0, sticky="e")
    opciones_biblioteca = tk.StringVar(ventana)
    opciones_biblioteca.set("Seleccionar")
    bibliotecas = obtener_bibliotecas()
    tk.OptionMenu(ventana,opciones_biblioteca, *bibliotecas.keys() ).grid(row=4, column=1, padx=5, pady=5, sticky="e")
    def agregar():
        try:
            isbnLibro = input_ISBN.get()
            titulo_libro = input_Titulo.get()
            autor_libro = input_autor.get()
            year_publicacion = input_yearP.get()
            name_biblioteca = opciones_biblioteca.get()
            if not(isbnLibro and titulo_libro and autor_libro and year_publicacion and name_biblioteca != "Seleccionar"):
                messagebox.showerror("ERROR", "Porfavor ingrese valores!")
                return
            if not year_publicacion.isdigit():
                messagebox.showerror("ERROR", "Ingrese solo números enteros!")
                return
            year_publicacion = int(year_publicacion)
            id_biblioteca = bibliotecas[name_biblioteca]
            agregar_libro(isbnLibro, titulo_libro, autor_libro, year_publicacion, id_biblioteca)
            messagebox.showinfo("Información", "Agregado con éxito!!")
        except Exception as ex:
            messagebox.showerror("Error!!", "Error no se pudo registrar el Libro",str(ex))
    tk.Button(ventana,text="Registrar libro", command=agregar).grid(row=0, column=2,padx=5,pady=5, sticky="e")