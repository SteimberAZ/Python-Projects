from tkinter import messagebox
import customtkinter as ctk
import time


ctk.set_appearance_mode("system")

ventana= ctk.CTk()
ventana.geometry("407x260")
ventana.resizable(False,False)
#ventana.iconbitmap("tu logo foramto .ico")


ventana.title("Smart RJ")

def Hora():
    tiempo_actual = time.localtime()
    Tiempo_arr = time.strftime("%a %d, %b %Y", tiempo_actual)
    tiempo = time.strftime("%I:%M:%S",tiempo_actual)

    ventana.fecha_tab.configure( text = f"{Tiempo_arr}")
    ventana.hora_tab.configure( text = f"{tiempo}")
    
    ventana.after(1000, Hora)

tiempo_inicio = False
tiempo_transcurrido = 0

def empezar():
    global tiempo_inicio
    if not tiempo_inicio:
        tiempo_inicio = True
        actualizar()
def detener():
    global tiempo_inicio
    if tiempo_inicio:
        tiempo_inicio= False
def resetear():
    global tiempo_transcurrido , tiempo_inicio
    tiempo_transcurrido = 0
    tiempo_inicio = 0
    ventana.crono_tab.configure(text= "00:00:00")
    actualizar()
def actualizar():
    global tiempo_transcurrido
    
    if tiempo_inicio:
        tiempo_transcurrido += 1
        hours = tiempo_transcurrido // 3600
        minutes = (tiempo_transcurrido // 60) % 60
        seconds = tiempo_transcurrido % 60
        time_string = f"{hours:02}:{minutes:02}:{seconds:02}"
        ventana.crono_tab.configure(text= time_string)
        ventana.crono_tab2.configure(text ="")
        ventana.after(1000, actualizar)
        
        



    

    
     
ventana.tabview = ctk.CTkTabview(ventana, width=380)
ventana.tabview.grid(row=0,column=0,padx = 13, pady= 0,sticky ="new")
ventana.tabview.add("Fecha y Hora")

#ventana de hora 
ventana.fecha_tab = ctk.CTkLabel(ventana.tabview.tab("Fecha y Hora"), text="",font=('skia', 15))
ventana.fecha_tab.place(x = 135, y= 5)
ventana.hora_tab = ctk.CTkLabel(ventana.tabview.tab("Fecha y Hora"), text="",font=('skia', 60))
ventana.hora_tab.place(x = 65, y= 50) 
ventana.tabview.add("Cronometro")
ventana.tabview.add("Calculadora")



#ventana de Cronometro
ventana.crono_tab = ctk.CTkLabel(ventana.tabview.tab("Cronometro"), text="",font=('skia', 60))
ventana.crono_tab.place(x = 65, y= 50) 
ventana.crono_tab2 = ctk.CTkLabel(ventana.tabview.tab("Cronometro"), text="00:00:00",font=('skia', 60))
ventana.crono_tab2.place(x = 65, y= 50) 
ventana.crono_but = ctk.CTkButton(ventana.tabview.tab("Cronometro"), text="Iniciar",command=empezar,font=('skia', 15),width= 80)
ventana.crono_but.place(x =30, y= 150) 

ventana.endo_but = ctk.CTkButton(ventana.tabview.tab("Cronometro"), text="Detener",command= detener,font=('skia', 15),width= 80)
ventana.endo_but.place(x = 140, y= 150)

ventana.res_but = ctk.CTkButton(ventana.tabview.tab("Cronometro"), text="Resetear",command= resetear,font=('skia', 15),width= 80,fg_color="green")
ventana.res_but.place(x = 250, y= 150)
#ventana de Calculadora

Barra = ctk.CTkEntry(ventana.tabview.tab("Calculadora"), width= 157, height= 30,font=('skia', 20),justify = "right")
Barra.place(x = 100, y= 5)


def button_7():
    new_text = Barra.get()
    new_text = 7
    Barra.insert(100,new_text)
boton7= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="7",width= 35, height= 35,font=('skia', 15),command=button_7)
boton7.place(x = 100, y= 40)

def button_8():
    new_text = Barra.get()
    new_text = 8
    Barra.insert(100,new_text)
boton8= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="8",width= 35, height= 35,font=('skia', 15),command=button_8)
boton8.place(x = 140, y= 40)

def button_9():
    new_text = Barra.get()
    new_text = 9
    Barra.insert(100,new_text)  
boton9= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="9",width= 35, height= 35,font=('skia', 15),command=button_9)
boton9.place(x = 180, y= 40)

def button_4():
    new_text = Barra.get()
    new_text = 4
    Barra.insert(100,new_text)
boton4= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="4",width= 35, height= 35,font=('skia', 15),command=button_4)
boton4.place(x = 100, y= 80)

def button_5():
    new_text = Barra.get()
    new_text = 5
    Barra.insert(100,new_text)
boton5= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="5",width= 35, height= 35,font=('skia', 15),command=button_5)
boton5.place(x = 140, y= 80)

def button_6():
    new_text = Barra.get()
    new_text = 6
    Barra.insert(100,new_text)
boton6= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="6",width= 35, height= 35,font=('skia', 15),command=button_6)
boton6.place(x = 180, y= 80)

def button_3():
    new_text = Barra.get()
    new_text = 3
    Barra.insert(100,new_text)
boton3= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="3",width= 35, height= 35,font=('skia', 15),command=button_3)
boton3.place(x = 100, y= 120)

def button_2():
    new_text = Barra.get()
    new_text = 2
    Barra.insert(100,new_text)
boton2= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="2",width= 35, height= 35,font=('skia', 15),command=button_2)
boton2.place(x = 140, y= 120)

def button_1():
    new_text = Barra.get()
    new_text = 1
    Barra.insert(100,new_text)
boton1= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="1",width= 35, height= 35,font=('skia', 15),command=button_1)
boton1.place(x = 180, y= 120)

def button_0():
    new_text = Barra.get()
    new_text = 0
    Barra.insert(100,new_text)
boton1= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="0",width= 35, height= 35,font=('skia', 15),command=button_0)
boton1.place(x = 100, y= 160)

def button_s():
    new_text = Barra.get()
    new_text = "+" 
    Barra.insert(100,new_text)
botonSuma= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="+",width= 35, height= 35,font=('skia', 15),command=button_s,fg_color="green")
botonSuma.place(x = 220, y= 40)

def button_r():
    new_text = Barra.get()
    new_text = "-"
    Barra.insert(100,new_text) 
botonRes= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="-",width= 35, height= 35,font=('skia', 15),command=button_r,fg_color="green")
botonRes.place(x = 220, y= 80)

def button_m():
    new_text = Barra.get()
    new_text = "*"
    Barra.insert(100,new_text)
botonMul= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="*",width= 35, height= 35,font=('skia', 15),command=button_m,fg_color="green")
botonMul.place(x = 220, y= 120)

def button_d():
    new_text = Barra.get()
    new_text = "/"
    Barra.insert(100,new_text) 
botonDiv= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="/",width= 35, height= 35,font=('skia', 15),command=button_d,fg_color="green")
botonDiv.place(x = 180, y= 160)

def Borrar_soloUNO():
    Barra.delete(0,1)
botonDiv= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text=">",width= 35, height= 35,font=('skia', 15),command=Borrar_soloUNO,fg_color="green")
botonDiv.place(x = 140, y= 160)      

def Resultado_4():
    try: 
        resultado = eval(Barra.get())
        Barra.delete(0,"end")
        Barra.insert(0,str(resultado))
        
    except:
        messagebox.showinfo("Resultado","Error")
    
botonResul= ctk.CTkButton(ventana.tabview.tab("Calculadora"),text="=",width= 35, height= 35,font=('skia', 15),command=Resultado_4,fg_color="green")
botonResul.place(x = 220, y= 160)      
Hora()
ventana.mainloop()