from tkinter import *
from tkinter import messagebox
import random
import json
import os
import sys
import pygame  

# Inicializa pygame
pygame.mixer.init()

def play_music():
    """Reproduce música de fondo."""
    pygame.mixer.music.load(r"C:\Users\randy\OneDrive\Documents\Python\.vscode\Megalovania.mp3") 
    pygame.mixer.music.play(-1)  #

def restart_program():
    """Reinicia el programa."""
    python = sys.executable
    os.execl(python, python, *sys.argv)

def update_points(ganar_perder):
    global puntos
    puntos += ganar_perder
    puntos_label.config(text=f"Total de puntos: {puntos}")
    with open('variable.json', 'w') as file:
        json.dump({'value': puntos}, file)

def check_guess():
    global numero_aleatorio
    try:
        numero_aleatorio = random.randint(1, 2)
        adivinador = int(entry.get())
        if adivinador == numero_aleatorio:
            update_points(10)
            messagebox.showinfo("Adivinador 3000", "¡Adivinaste! Tienes 10 puntos más.")
        else:
            update_points(-5)
            messagebox.showinfo("Adivinador 3000", "Perdiste. Tienes 5 puntos menos.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido.")


ventana = Tk()
ventana.title("Adivinador 3000")
ventana.geometry("300x400")

Label(ventana, text="Elige un número del 1 al 2").place(x=30, y=40)

entry = Entry(ventana)
entry.place(x=30, y=60)

Button(ventana, text="Adivinar", command=check_guess).place(x=30, y=90)
Button(ventana, text="Reiniciar", command=restart_program).place(x=100, y=90)

try:
    with open('variable.json', 'r') as file:
        data = json.load(file)
        puntos = data["value"]
except FileNotFoundError:
    puntos = 0

puntos_label = Label(ventana, text=f"Total de puntos: {puntos}")
puntos_label.place(x=30, y=10)

# Inicia la música automáticamente
play_music()

ventana.mainloop()
