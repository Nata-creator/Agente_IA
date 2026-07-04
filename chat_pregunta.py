import tkinter as tk
from tkinter import scrolledtext, messagebox
from conexion_agente import ConectarConAgente

def enviar_mensaje():
    """Obtiene el texto del usuario, lo muestra y responde."""
    mensaje = entrada.get().strip().lower()

    if not mensaje:
        messagebox.showwarning("Aviso", "Escribe algo antes de enviar.")
        return

    # Mostrar mensaje del usuario
    chat.insert(tk.END, f"Tú: {mensaje}\n")

    # Buscar respuesta
    conexion_agente = ConectarConAgente()
    respuesta = conexion_agente.obtener_respuesta_modelo_agente(mensaje)
    chat.insert(tk.END, f"Bot: {respuesta}\n\n")

    # Hacer scroll automático
    chat.yview(tk.END)

    # Limpiar entrada
    entrada.delete(0, tk.END)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Chat Nasytu")
ventana.geometry("400x400")

# Área de chat con scroll
chat = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, state="normal")
chat.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entrada de texto
entrada = tk.Entry(ventana)
entrada.pack(padx=10, pady=5, fill=tk.X)

# Botón de enviar
btn_enviar = tk.Button(ventana, text="Enviar", command=enviar_mensaje)
btn_enviar.pack(pady=5)

# Permitir enviar con Enter
ventana.bind("<Return>", lambda event: enviar_mensaje())
ventana.state('zoomed')  # En Windows maximiza la ventana
ventana.mainloop()
