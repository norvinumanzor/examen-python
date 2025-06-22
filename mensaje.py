import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    """Muestra un mensaje de alerta"""
    messagebox.showinfo("Mensaje","18 años")

def mostrar_mensaje1():
    """Muestra un mensaje de alerta"""
    messagebox.showinfo("Mensaje","Totogalpa")

root = tk.Tk()
root.title("Examen primer parcial - Norvin Umanzor")

#Agregar una etiqueta de titulo con el nombre "nombre de usuario"
etiqueta_usuario = tk.Label(root, text="Mi nombre es Norvin")
etiqueta_usuario.pack(pady=10)

boton= tk.Button(root, text="Edad", command=mostrar_mensaje)
boton.pack(side='left', padx=5, pady=10)

boton= tk.Button(root, text="Vivo en", command=mostrar_mensaje1)
boton.pack(side='right', padx=5, pady=10)

# Configurar tamaño de la ventana 
root.geometry("300x200")
#EStablecer un color de fondo
root.configure(bg='lightblue')

 # Ejecutar el bucle principal de la aplicacion
root.mainloop()