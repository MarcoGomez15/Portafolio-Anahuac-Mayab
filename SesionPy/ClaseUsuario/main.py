from ClaseUsuario import Usuario
import tkinter as tk
from tkinter import simpledialog, messagebox

#Creacion de la ventana
root = tk.Tk()
root.withdraw() #Oculta la ventana principal solo veremos cuadros de dialogo

# Creación del objeto
# nombreObjeto = nombreClase()
maestra = Usuario()

maestra.nombre = simpledialog.askstring("Maestra", "Ingrese el nombre")
maestra.apellidos = simpledialog.askstring("Maestra", "Ingrese el apellido")
maestra.edad = simpledialog.askinteger("Maestra", "Ingrese la edad")

messagebox.showinfo("Maestra", maestra.iniciarSesion())
messagebox.showinfo("Maestra", maestra.cerrarSesion())
messagebox.showinfo("Maestra", maestra.hacerReporte())

#alumno = Usuario("Tom", "Cruise", 64)

# Asignar valores a los atributos
#maestra.apellidos = "Hernandez Olan"
#maestra.nombre = "Lizbeth"
#maestra.edad = 42

# Llamada (invocación) de métodos
#maestra.iniciarSesion()
#maestra.cerrarSesion()
#maestra.hacerReporte()

print()

#alumno.iniciarSesion()
#alumno.cerrarSesion()
#alumno.hacerReporte()