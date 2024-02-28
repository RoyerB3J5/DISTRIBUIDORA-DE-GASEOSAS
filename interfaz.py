from tkinter import *
from databaseadmi import *
from tkinter import messagebox
from tkinter import ttk
from principaladmi import *
from principalpedido import *
from ingreso_registro import *

pagina = Tk()
pagina.geometry("700x600")
pagina.config(bg="light cyan")
pagina.title("PEDIDO DE GASEOSAS")
frame = Frame(pagina)
frame.pack(expand=True)
etiqueta = Label(pagina, text="PROVEEDORA DE GASEOSAS",fg = "black", bg = "light cyan" ,font=("courier new", 25, "bold")).place(x=150,y=50)
imagen = PhotoImage(file="gaseosas.png")
imagen_label = Label(pagina, image=imagen, bg = "light cyan")
imagen_label.place (x =200,y =90)


boton1=Button(pagina, text = "ADMINISTRACION", bg = "light grey", font = ("courier new", 20, "bold"), command = seguridad_admi,border = 5).place(x = 80, y = 400)
boton2 = Button(pagina, text = "PEDIDO", bg = "light grey", font = ("courier new", 20, "bold"),command=ventana_ped, border = 5)
boton2.place(x = 450, y = 400)

pagina.mainloop()
