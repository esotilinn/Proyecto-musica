import tkinter as tk
from tkinter import messagebox
import os
import pygame

pygame.mixer.init()

directorio_letras = 'Letras'
directorio_mp3 = 'MP3'

def cargar_letra(cancion):
    try:
        with open(os.path.join(directorio_letras, f"{cancion}.txt"), 'r', encoding='utf-8') as archivo:
            letra = archivo.read()
        return letra
    except FileNotFoundError:
        return None

def obtener_canciones():
    canciones = []
    for archivo in os.listdir(directorio_letras):
        if archivo.endswith(".txt"):
            canciones.append(archivo.replace(".txt", ""))
    return canciones

def reproducir_cancion(cancion):
    try:
        pygame.mixer.music.load(os.path.join(directorio_mp3, f"{cancion}.mp3"))
        pygame.mixer.music.play()
    except pygame.error:
        messagebox.showerror("Error", "No se pudo reproducir la canción.")

def seleccionar_cancion():
    cancion = combo_canciones.get()
    if cancion:
        letra = cargar_letra(cancion)
        if letra:
            texto_letra.config(state=tk.NORMAL)
            texto_letra.delete(1.0, tk.END)
            texto_letra.insert(tk.END, letra)
            texto_letra.config(state=tk.DISABLED)
            reproducir_cancion(cancion)
        else:
            messagebox.showerror("Canción no encontrada", "La letra de la canción no está disponible.")
    else:
        messagebox.showerror("Error", "Por favor, selecciona una canción.")

# ... (el resto del código sigue igual)

def detener_cancion():
    pygame.mixer.music.stop()

# 🌟 Ventana principal decorada
ventana = tk.Tk()
ventana.title("🎵 ¿Puedo dedicarte algo? 🎶")
ventana.geometry("900x600")
ventana.configure(bg="#1e1e2f")

# Fuente y colores
fuente_titulo = ("Helvetica", 16, "bold")
fuente_normal = ("Helvetica", 12)
color_fondo = "#1e1e2f"
color_texto = "#ffffff"
color_boton = "#4caf50"
color_boton_texto = "#ffffff"
color_boton_detener = "#e53935"

# Etiqueta
etiqueta = tk.Label(ventana, text="Selecciona una canción:", bg=color_fondo, fg=color_texto, font=fuente_titulo)
etiqueta.pack(pady=15)

# Combobox
canciones = obtener_canciones()
combo_canciones = tk.StringVar()
combobox = tk.OptionMenu(ventana, combo_canciones, *canciones)
combobox.config(bg="#3c3f58", fg=color_texto, font=fuente_normal, width=30)
combobox["menu"].config(bg="#3c3f58", fg=color_texto)
combobox.pack(pady=10)

# Frame para botones juntos
frame_botones = tk.Frame(ventana, bg=color_fondo)
frame_botones.pack(pady=15)

# Botón reproducir
boton_buscar = tk.Button(
    frame_botones,
    text="▶ Reproducir",
    command=seleccionar_cancion,
    bg=color_boton,
    fg=color_boton_texto,
    font=fuente_normal,
    padx=10,
    pady=5
)
boton_buscar.pack(side=tk.LEFT, padx=10)

# Botón detener
boton_detener = tk.Button(
    frame_botones,
    text="⏹️ Parar",
    command=detener_cancion,
    bg=color_boton_detener,
    fg=color_boton_texto,
    font=fuente_normal,
    padx=10,
    pady=5
)
boton_detener.pack(side=tk.LEFT, padx=10)

# Área de texto decorada
texto_letra = tk.Text(
    ventana, 
    wrap=tk.WORD, 
    height=20, 
    width=90, 
    state=tk.DISABLED,
    bg="#2c2f4a", 
    fg=color_texto,
    font=("Courier New", 12),
    relief="flat"
)
texto_letra.pack(pady=10)

ventana.mainloop()
