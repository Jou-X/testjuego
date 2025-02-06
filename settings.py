import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Programa")

# Añadir un widget de etiqueta (Label) a la ventana
etiqueta = tk.Label(ventana, text="¡Hola, mundo!")
etiqueta.pack(padx=20, pady=20)

# Añadir un botón para cerrar la ventana
boton_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.quit)
boton_cerrar.pack(pady=10)

# Iniciar el bucle principal de la ventana
ventana.mainloop()