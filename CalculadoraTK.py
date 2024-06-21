from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import PhotoImage


Ventana = tk.Tk()
Ventana.title("Calculadora")
Ventana.geometry("400x150")
#Ventana.iconbitmap("tu logo formato .ico")
Ventana.resizable(False,False)

#label_img = PhotoImage(file="tu fondo")
#label_con_imagen = Label(Ventana, image = label_img)
#label_con_imagen.pack(pady=0)

def Sumacion():
        Otorgado1 = int(Numero1.get())
        Otorgado2 = int(Numero2.get())
        messagebox.showinfo("Tu suma es = ",Otorgado1 + Otorgado2,)
    
def Multuplicacion():
        Otorgado1 = int(Numero1.get())
        Otorgado2 = int(Numero2.get())
        messagebox.showinfo("Tu multiplicacion es = ",Otorgado1 * Otorgado2,)       

def Restacion():
        Otorgado1 = int(Numero1.get())
        Otorgado2 = int(Numero2.get())
        messagebox.showinfo("Tu resta es = ",Otorgado1 - Otorgado2,)       

def Diviciasion():
        Otorgado1 = int(Numero1.get())
        Otorgado2 = int(Numero2.get())
        messagebox.showinfo("Tu Division es = ",Otorgado1 / Otorgado2,)    

Label1= Label(Ventana, text="Ingrese un numero =",font="skia 8 bold",background="#f705db").place(x=47, y=10)
Label2= Label(Ventana, text="Ingrese otro numero =",font="skia 8 bold",background="#f705db").place(x=40, y=35)

Sumar = Button(Ventana, text="Sumar",command=Sumacion,font="skia 8 bold",background="#f705db").place(x=140, y=80)
Restar = Button(Ventana, text="Restar",command=Restacion,font="skia 8 bold",background="#f705db").place(x=195, y=80)
Multiplicar = Button(Ventana, text="Multiplicar",command=Multuplicacion,font="skia 8 bold",background="#f705db").place(x=65, y=80)
Divicion = Button(Ventana, text="Dividir",command=Diviciasion,font="skia 8 bold",background="#f705db").place(x=250, y=80)



Numero1 = Entry(Ventana)
Numero1.place(x=170, y=10)
Numero2 = Entry(Ventana)
Numero2.place(x=170, y=35)

Ventana.mainloop()


