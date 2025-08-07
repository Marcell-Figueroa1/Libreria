# Importamos la libreria tkinter
import tkinter as tk
# Importamos el archivo formulario_biblioteca para ocupar la función crear_biblioteca
from gui.formulario_biblioteca import crear_biblioteca

# Creamos una ventana
ventana = tk.Tk()
# Ponemos titulo a la ventana
ventana.title("Formulario")

# Dimensiones de la ventana
alturaV = 200
anchoV = 400

# Dimensiones de la pantalla
AlturaPantalla = ventana.winfo_screenheight()
AnchoPantalla = ventana.winfo_screenwidth()

# Calcular posición x, y para centrar
x = (AnchoPantalla - anchoV) // 2
y = (AlturaPantalla - alturaV) // 2

# Posición de la ventana en pantalla (Centro)
ventana.geometry(f"{anchoV}x{alturaV}+{x}+{y}")

crear_biblioteca(ventana)

ventana.mainloop()