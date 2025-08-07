import tkinter as tk
from models.biblioteca_model import agregar_biblioteca
from tkinter import messagebox
from gui.formulario_libro import crear_libro
def crear_biblioteca(interfaz):
    # Titulo de la pestaña
    interfaz.title("Formulario biblioteca")
    # Label y input del id de la biblioteca
    tk.Label(interfaz,text="Id biblioteca: ").grid(row=0, column=0, sticky="e")
    input_id = tk.Entry(interfaz)
    input_id.grid(row=0, column=1, padx=5, pady=5, sticky="e")
    # Label y input del nombre de la biblioteca
    tk.Label(interfaz,text="Nombre biblioteca: ").grid(row=1, column=0, sticky="e")
    input_nombreB = tk.Entry(interfaz)
    input_nombreB.grid(row=1, column=1, padx=5, pady=5, sticky="e")
    # Label y input de ubicación
    tk.Label(interfaz,text="Ubicación: ").grid(row=2, column=0, sticky="e")
    input_ubicacion = tk.Entry(interfaz)
    input_ubicacion.grid(row=2, column=1, padx=5, pady=5, sticky="e")
    def agregar():
        try:
            biblioteca_id = input_id.get()
            n_biblioteca = input_nombreB.get()
            ubicacion_b = input_ubicacion.get()
            agregar_biblioteca(biblioteca_id, n_biblioteca, ubicacion_b)
        except Exception as ex:
            messagebox.showerror("Error!!", "No se pudo registrar la biblioteca: ",str(ex))
    tk.Button(interfaz,text="Registrar biblioteca", command=agregar).grid(row=0, column=2,padx=5,pady=5, sticky="e")
    tk.Button(interfaz,text="Registrar libro", command=crear_libro).grid(row=1, column=2,padx=5,pady=5, sticky="e")