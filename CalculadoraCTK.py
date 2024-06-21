import tkinter
from tkinter import messagebox
import customtkinter as ctk

ctk.set_appearance_mode("system")
  
app = ctk.CTk() 
app.geometry("410x400")
app.resizable(False,False)

#Funciones de operadores

def button_1():
    new_text = Barra.get()
    new_text = 7
    Barra.insert(100,new_text)
def button_2():
    new_text = Barra.get()
    new_text = 8
    Barra.insert(100,new_text) 
def button_3():
    new_text = Barra.get()
    new_text = 9
    Barra.insert(100,new_text)  
def button_4():
    new_text = Barra.get()
    new_text = 4
    Barra.insert(100,new_text)
def button_5():
    new_text = Barra.get()
    new_text = 5
    Barra.insert(100,new_text) 
def button_6():
    new_text = Barra.get()
    new_text = 6
    Barra.insert(100,new_text) 
def button_7():
    new_text = Barra.get()
    new_text = 1
    Barra.insert(100,new_text)
def button_8():
    new_text = Barra.get()
    new_text = 2
    Barra.insert(100,new_text) 
def button_9():
    new_text = Barra.get()
    new_text = 3
    Barra.insert(100,new_text)
def button_0():
    new_text = Barra.get()
    new_text = 0
    Barra.insert(100,new_text) 
    
#Funciones de resta y igual 
        
def Resultado_4():
    try: 
        resultado = eval(Barra.get())
        Barra.delete(0,"end")
        Barra.insert(0,str(resultado))
        
    except:
        messagebox.showinfo("Resultado","Error")
    
#Funciones de borrado
    
def Borrar_4():
    Barra.delete(0,"end") 
    
def Borrar_soloUNO():
    Barra.delete(1,10)     
    
#Funciones de operadores

def button_s():
    new_text = Barra.get()
    new_text = "+" 
    Barra.insert(100,new_text)
def button_r():
    new_text = Barra.get()
    new_text = "-"
    Barra.insert(100,new_text) 
def button_m():
    new_text = Barra.get()
    new_text = "*"
    Barra.insert(100,new_text)
def button_d():
    new_text = Barra.get()
    new_text = "/"
    Barra.insert(100,new_text) 
#Fuente   
font1=ctk.CTkFont(family='skia', size= 24)


#Barra donde se ponen los numeros

Barra = ctk.CTkEntry(master=app,width= 327,height=(50),font=('skia', 24), justify='right')
Barra.place(relx=0.05,rely=0.1)


# Botones de numeros

button1 =ctk.CTkButton(master=app, text="7", command=button_1,width=(80),height=(50),font= font1)
button1.place(relx=0.05, rely=0.3)
button2 = ctk.CTkButton(master=app, text="8", command=button_2,width=(80),height=(50),font= font1)
button2.place(relx=0.25, rely=0.3)
button3 = ctk.CTkButton(master=app, text="9", command=button_3,width=(80),height=(50),font=('skia', 24))
button3.place(relx=0.45, rely=0.3)
button4 = ctk.CTkButton(master=app, text="4", command=button_4,width=(80),height=(50),font=('skia', 24))
button4.place(relx=0.05, rely=0.45)
button5 = ctk.CTkButton(master=app, text="5", command=button_5,width=(80),height=(50),font=('skia', 24))
button5.place(relx=0.25, rely=0.45)
button6 = ctk.CTkButton(master=app, text="6", command=button_6,width=(80),height=(50),font=('skia', 24))
button6.place(relx=0.45, rely=0.45)
button7 = ctk.CTkButton(master=app, text="1", command=button_7,width=(80),height=(50),font=('skia', 24))
button7.place(relx=0.05, rely=0.6)
button8 = ctk.CTkButton(master=app, text="2", command=button_8,width=(80),height=(50),font=('skia', 24))
button8.place(relx=0.25, rely=0.6)
button9 = ctk.CTkButton(master=app, text="3", command=button_9,width=(80),height=(50),font=('skia', 24))
button9.place(relx=0.45, rely=0.6)
button0 = ctk.CTkButton(master=app, text="0", command=button_0,width=(80),height=(50),font=('skia', 24))
button0.place(relx=0.05, rely=0.75)

#Botones de operadores

button_Suma = ctk.CTkButton(master=app, text="+", command=button_s,width=(80),height=(50),fg_color="green",font=('skia', 24))
button_Suma.place(relx=0.65, rely=0.3)
button_Res = ctk.CTkButton(master=app, text="-", command=button_r,width=(80),height=(50),fg_color="green",font=('skia', 24))
button_Res.place(relx=0.65, rely=0.45)
button_Mul = ctk.CTkButton(master=app, text="x", command=button_m,width=(80),height=(50),fg_color="green",font=('skia', 24))
button_Mul.place(relx=0.65, rely=0.6)
button_Div = ctk.CTkButton(master=app, text="/", command=button_d,width=(80),height=(50),fg_color="green",font=('skia', 24))
button_Div.place(relx=0.45, rely=0.75)

#Borrar

button_Del = ctk.CTkButton(master=app, text="Del", command=Borrar_4,width=(80),height=(50),fg_color="green",font=('skia', 24))
button_Del.place(relx=0.25, rely=0.75)
button_Del1 = ctk.CTkButton(master=app, text="Borrar", command=Borrar_soloUNO,width=(327),height=(10),fg_color="green",font=('skia', 12))
button_Del1.place(relx=0.05, rely=0.24)

#Igual

button_Del = ctk.CTkButton(master=app, text="=", command=Resultado_4,width=(80),height=(50),fg_color="green",font=('skia', 24))
button_Del.place(relx=0.65, rely=0.75)

app.mainloop()