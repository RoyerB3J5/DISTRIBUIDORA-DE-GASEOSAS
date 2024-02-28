from tkinter import *
from databaseadmi import *
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import os
from datetime import datetime
import mysql.connector



class App:

    def __init__(self, master):
        self.frame = master
        self.DrawEntry()
        self.DrawButtons()
        self.DrawLabel()
        self.DrawList()
        #self.loadImage()

    def DrawLabel(self):
        self.lbl_title = Label(self.frame, foreground="black",font=("arial",15,"bold"), background="light cyan",text="AGREGAR").place(x=120, y=70)
        self.lbl_name = Label(self.frame, foreground="black",font=("arial",13,"bold"), background="light cyan",text="Nombre:").place(x=60, y=110)
        self.lbl_six = Label(self.frame, foreground="black",font=("arial",13,"bold"), background="light cyan", text="Cantidad(six pack):").place(x=60, y=160)
        self.lbl_price = Label(self.frame, foreground="black",font=("arial",13,"bold"), background="light cyan", text="Precio:").place(x=60, y=210)
        self.lbl_liter = Label(self.frame, foreground="black",font=("arial",13,"bold"), background="light cyan", text="Capacidad (L):").place(x=60, y=260)


    def DrawEntry(self):
        self.name = StringVar()
        self.six = StringVar()
        self.price = StringVar()
        self.liter = StringVar()
        self.txt_name = Entry(self.frame,font=('Arial', 12),relief="flat", background="white" ,textvariable=self.name)
        self.txt_name.place(x=140, y=110, height=25, width=150)
        self.txt_six = Entry(self.frame,font=('Arial', 12),relief="flat", background="white" ,textvariable=self.six)
        self.txt_six.place(x=240, y=160, height=25, width=50)
        self.txt_price = Entry(self.frame,font=('Arial', 12),relief="flat", background="white" ,textvariable=self.price)
        self.txt_price.place(x=140, y=210, height=25, width=150)
        self.txt_liter = Entry(self.frame,font=('Arial', 12),relief="flat", background="white" ,textvariable=self.liter)
        self.txt_liter.place(x=200, y=260, height=25, width=90)
        # Asocia la función convertir_a_mayusculas al evento de cambio de texto en el Entry
        self.txt_name.bind("<KeyRelease>", self.convertir_a_mayusculas)

        
    def convertir_a_mayusculas(self,event):
        # Obtiene el valor actual del Entry y lo convierte a mayúsculas
        nuevo_valor = self.txt_name.get().upper()
        self.name.set(nuevo_valor)


    
    def DrawButtons(self):
        self.btn_confirm = Button(self.frame,foreground="white", text="Guardar",borderwidth=2,relief="flat", cursor="hand1",overrelief="raise",background="blue4", command=lambda:self.confirmProcess()).place(x=1100, y=350, width=90)
        self.btn_cancel = Button(self.frame, text="Cancelar",foreground="white",borderwidth=2,relief="flat", cursor="hand1",overrelief="raise",background="red", command= lambda:self.canceProcess()).place(x=1200, y=350, width=90)



    def DrawList(self):
        self.list_elemts = ttk.Treeview(self.frame, columns=(1, 2, 3, 4,5), show="headings", height="8")

        # --- STYLE ---	
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="Royalblue4",relief="flat",foreground="white")
        style.map("Treeview", background=[('selected', 'yellow')], foreground=[('selected', 'black')])

        #--- Evento---AL darle doble click a un elemento de la tabla, abrira el metodo getRow
        self.list_elemts.bind("<Double 1>", self.getRow)
        #---- fin ---

        self.list_elemts.heading(1, text="Codigo")
        self.list_elemts.heading(2, text="Nombre")
        self.list_elemts.heading(3, text="Cantidad(six pack)")
        self.list_elemts.heading(4, text="Precio")
        self.list_elemts.heading(5, text="Capacidad (L)")
        self.list_elemts.column(1, anchor=CENTER)
        self.list_elemts.column(2, anchor=CENTER)
        self.list_elemts.column(3, anchor=CENTER)
        self.list_elemts.column(4, anchor=CENTER)
        self.list_elemts.column(5, anchor=CENTER)

        # -- LLENAR LIST--
        d = Data()
        self.rows = d.returnAllElements()
        for i in self.rows:
            self.list_elemts.insert('', 'end', values=i)
        # ----- fin -----

        self.list_elemts.place(x=340, y=90)

        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.list_elemts.yview)
        scrollbar.place(x=1340, y=90, height=190)  # Ajusta la posición y altura de la barra de desplazamiento

    # Configuración del Treeview para usar la barra de desplazamiento
        self.list_elemts.configure(yscrollcommand=scrollbar.set)

    
    def getRow(self, event):
     self.na = StringVar()
     self.sx = StringVar()
     self.pr = StringVar()
     self.li = StringVar()
    
    # Obtén la fila seleccionada
     item = self.list_elemts.item(self.list_elemts.focus())
    
     if item is not None:
        n = item['values'][1]
        s = item['values'][2]
        p = item['values'][3]
        l = item['values'][4]
        
        self.na.set(n)
        self.sx.set(s)
        self.pr.set(p)
        self.li.set(l)
        
        pop = Toplevel(self.frame)
        pop.geometry("400x250")
        lbl_tittle = Label(pop, text="ACTUALIZAR", font=("courier new", 18, "bold")).place(x=125, y=10)
        lbl_n = Label(pop, text="Nombre:", font=('Arial', 12), fg="black").place(x=50, y=40)
        lbl_s = Label(pop, text="Cantidad(six pack):", font=('Arial', 12), fg="black").place(x=50, y=80)
        lbl_p = Label(pop, text="Precio:", font=('Arial', 12), fg="black").place(x=50, y=120)
        lbl_l = Label(pop, text="Capacidad (L):", font=('Arial', 12), fg="black").place(x=50, y=160)
        txt_n = Entry(pop, textvariable=self.na).place(x=200, y=40)
        txt_s = Entry(pop, textvariable=self.sx).place(x=200, y=80)
        txt_p = Entry(pop, textvariable=self.pr).place(x=200, y=120)
        txt_l = Entry(pop, textvariable=self.li).place(x=200, y=160)
        
        # Utiliza una función lambda para pasar la fila seleccionada
        btn_change = Button(pop, text="Actualizar", relief="flat", background="green2",
                            foreground="white", command=lambda: self.editar(item)).place(x=180, y=200, width=90)
        btn_delete = Button(pop, text="Eliminar", relief="flat", background="red",
                            foreground="white", command=lambda: self.eliminar(n)).place(x=290, y=200, width=90)

    def eliminar(self, n,p):
      d = Data()
      d.Delete(n,p)
      messagebox.showinfo(title="Eliminación", message="Se ha eliminado el elemento")
      self.ClearList()
      self.DrawList()
      self.ClearEntry()

    def editar(self, item):
    # Obtén los nuevos valores de los Entry widgets
        na = self.na.get()
        sx = self.sx.get()
        pr = self.pr.get()
        li = self.li.get()

    # Actualiza la fila seleccionada con los nuevos valores
        updated_item = [item['values'][0], na, sx, pr, li]
        d = Data()
        d.UpdateItem(updated_item, item['values'][0])
        messagebox.showinfo(title="Actualización", message="Se han actualizado los datos")
        self.ClearList()
        self.DrawList()
        self.ClearEntry()



    def ClearList(self):
        self.list_elemts.delete(*self.list_elemts.get_children())
    
    def canceProcess(self):
        self.ClearEntry()

    
    def ClearEntry(self):
        self.name.set("")
        self.six.set("")
        self.price.set("")
        self.liter.set("")
    

    
    def confirmProcess(self):
        if self.name.get() != "" and self.six.get() != "" and self.price.get() != ""and self.liter.get() != "":
            d = Data()
            arr = [self.name.get(), self.six.get(), self.price.get(),self.liter.get()]
            d.InsertItems(arr)
            messagebox.showinfo(title="Alerta", message="Se inserto correctamente!")
            self.ClearList()
            self.DrawList()
            self.ClearEntry()
        else:
            messagebox.showinfo(title="Error", message="Debe llenar los campos para poder guardar!")
                
class App2():
    def __init__(self, master):
        self.frame = master
        self.d = Data_1admi()
        self.grafico()
        self.imagen()
        self.table()
        self.label()
        self.button()
        
    def grafico(self):
        
        valor_grafico = self.d.circulo()

        labels = [row[0] for row in valor_grafico]
        values = [row[1] for row in valor_grafico]

        plt.figure(figsize=(6, 5))
        plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title("Porcentaje de ventas de gaseosas")
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        if os.path.exists("grafico_circulo.png"):
            os.remove("grafico_circulo.png")

        plt.savefig("grafico_circulo.png") 

    def imagen(self):
    
        self.img  = PhotoImage(file="grafico_circulo.png")
        label_img = Label(self.frame, image = self.img)
        label_img.image = self.img
        label_img.place(x = 50, y = 70)

    def table(self):
        
        self.list_elemts = ttk.Treeview(self.frame, columns=(1, 2), show="headings", height= "5")

        # --- STYLE ---	
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="Royalblue4",relief="flat",foreground="white")

        
        self.list_elemts.heading(1, text="Gaseosa")
        self.list_elemts.heading(2, text="Cantidad")
        self.list_elemts.column(1, anchor=CENTER, width=170)
        self.list_elemts.column(2, anchor=CENTER, width= 170)
    
        # -- LLENAR LIST--
        
        self.rows = self.d.circulo()
        for i in self.rows:
            self.list_elemts.insert('', 'end', values=i)
        # ----- fin -----

        self.list_elemts.place(x=700, y=150)

        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.list_elemts.yview)
        scrollbar.place(x=1044, y=150, height=130)  # Ajusta la posición y altura de la barra de desplazamiento

    # Configuración del Treeview para usar la barra de desplazamiento
        self.list_elemts.configure(yscrollcommand=scrollbar.set)

    def label(self):
        maxima = self.d.max_gaseosa()
        total = self.d.total()

        self.label_total =  Label(self.frame, foreground="black",font=("arial",14,"bold"), background="light cyan",text="Cantidad de gaseosas vendidas:").place(x=700, y=350)
        self.label_total_val =  Label(self.frame, foreground="black",font=("arial",14), background="light cyan",text=total).place(x=860, y=400)

        self.label_gaseosa =  Label(self.frame, foreground="black",font=("arial",14,"bold"), background="light cyan",text="La marca de gaseosa más vendida es:").place(x=700, y=450)
        self.label_gaseosa_val =  Label(self.frame, foreground="black",font=("arial",14), background="light cyan",text=maxima).place(x=850, y=500)
    
    def button(self):
        self.back = Button(self.frame, text = "ATRÁS", bg = "red3", fg = "white", font = ("courier new", 17, "bold"), border = 5, command = self.frame.destroy)
        self.back.place(x=950,y=580)

    
class App3():
    def __init__(self, master):
        self.frame = master
        self.label()
        self.entry()
        self.button()
        

    def label(self):
        self.label_inicio = Label(self.frame, foreground="black",font=("arial",14,"bold"), background="light cyan",text="Desde (YYYY-MM-DD):").place(x=50, y=100)
        self.label_fin = Label(self.frame, foreground="black",font=("arial",14,"bold"), background="light cyan",text="Fin (YYYY-MM-DD):").place(x=50, y=200)

    

    def formatear_fecha(self,event, entry):
    # Obtenemos la fecha del Entry
      self.fecha_str = entry.get()
    
      try:
        # Convertimos la fecha a un objeto datetime
        fecha = datetime.strptime(self.fecha_str, "%Y-%m-%d")
        # Formateamos la fecha en el formato de MySQL TIMESTAMP
        fecha_mysql = fecha.strftime("%Y-%m-%d")
        entry.delete(0, END)
        entry.insert(0, fecha_mysql)
      except ValueError:
        print("Error: Formato de fecha incorrecto")
    
    def entry(self):
        self.entry_fecha_incio = Entry(self.frame,font=('Arial', 12),relief="flat", background="white")
        self.entry_fecha_incio.place(x=300, y=100, height=25, width=150)
        self.entry_fecha_incio.bind('<FocusOut>', lambda event: self.formatear_fecha(event,self.entry_fecha_incio))

        self.entry_fecha_fin = Entry(self.frame,font=('Arial', 12),relief="flat", background="white")
        self.entry_fecha_fin.place(x=300, y=200, height=25, width=150)
        self.entry_fecha_fin.bind('<FocusOut>', lambda event: self.formatear_fecha(event,self.entry_fecha_fin))

    def obtener_fecha_inicio(self):
        return self.entry_fecha_incio.get()

    def obtener_fecha_fin(self):
        return self.entry_fecha_fin.get()

    def button(self):
        self.generar = Button(self.frame, text = "GENERAR", bg = "blue4", fg = "white", font = ("courier new", 17, "bold"), border = 5, command=self.abrir_reporte)
        self.generar.place(x=180,y=300)

    def abrir_reporte(self):
        reporte_cliente_2(self)




class App4():
    def __init__(self, master,app3_instance):
        self.frame = master
        self.app3_instance = app3_instance
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Hoyesdia21",
            database = "proyecto")
        self.cursor = self.conn.cursor()
        self.tabla_cliente()
        self.button()
        
        

    def cliente(self,fecha_inicio, fecha_fin):
        sql = f"""SELECT C.PedidoId, C.Nombre, C.NombreTienda, D.Calle, D.Numero, C.Ruc, C.Telefono,  C.Fecha 
		          FROM Cliente C,Detalle_Cliente D WHERE C.PedidoID = D.PedidoID AND DATE(C.Fecha) BETWEEN '{fecha_inicio}' AND '{fecha_fin}' """
        self.cursor.execute(sql)
        dato = self.cursor.fetchall()
        return dato    

    def tabla_cliente(self):
        self.list_elemts = ttk.Treeview(self.frame, columns=(1, 2,3,4,5,6,7,8), show="headings", height= "5")

        # --- STYLE ---	
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="Royalblue4",relief="flat",foreground="white")

        
        self.list_elemts.heading(1, text="ID")
        self.list_elemts.heading(2, text="CLIENTE")
        self.list_elemts.heading(3, text="NOMBRE DE TIENDA")
        self.list_elemts.heading(4, text="CALLE")
        self.list_elemts.heading(5, text="NUMERO")
        self.list_elemts.heading(6, text="RUC")
        self.list_elemts.heading(7, text="TELÉFONO")
        self.list_elemts.heading(8, text="FECHA")
        
        self.list_elemts.column(1, anchor=CENTER, width=150)
        self.list_elemts.column(2, anchor=CENTER, width= 150)
        self.list_elemts.column(3, anchor=CENTER, width=150)
        self.list_elemts.column(4, anchor=CENTER, width= 150)
        self.list_elemts.column(5, anchor=CENTER, width=150)
        self.list_elemts.column(6, anchor=CENTER, width= 150)
        self.list_elemts.column(7, anchor=CENTER, width=150)
        self.list_elemts.column(8, anchor=CENTER, width= 150)
    
        # -- LLENAR LIST--
        
        fecha_inicio = self.app3_instance.obtener_fecha_inicio()
        fecha_fin = self.app3_instance.obtener_fecha_fin()
        # Consultar la base de datos con las fechas obtenidas
        self.rows = self.cliente(fecha_inicio, fecha_fin)
        for i in self.rows:
            self.list_elemts.insert('', 'end', values=i)

        self.list_elemts.place(x=50, y=70)

        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.list_elemts.yview)
        scrollbar.place(x=1250, y=70, height=130)  # Ajusta la posición y altura de la barra de desplazamiento

    # Configuración del Treeview para usar la barra de desplazamiento
        self.list_elemts.configure(yscrollcommand=scrollbar.set)

    def button(self):
        self.back = Button(self.frame, text = "ATRÁS", bg = "red3", fg = "white", font = ("courier new", 17, "bold"), border = 5, command = self.frame.destroy)
        self.back.place(x=1150,y=220)

class App5():
    def __init__(self, master):
        self.frame = master
        self.label()
        self.entry()
        self.button()
        

    def label(self):
        self.label_inicio = Label(self.frame, foreground="black",font=("arial",14,"bold"), background="light cyan",text="Desde (YYYY-MM-DD):").place(x=50, y=100)
        self.label_fin = Label(self.frame, foreground="black",font=("arial",14,"bold"), background="light cyan",text="Fin (YYYY-MM-DD):").place(x=50, y=200)

    

    def formatear_fecha(self,event, entry):
    # Obtenemos la fecha del Entry
      self.fecha_str = entry.get()
    
      try:
        # Convertimos la fecha a un objeto datetime
        fecha = datetime.strptime(self.fecha_str, "%Y-%m-%d")
        # Formateamos la fecha en el formato de MySQL TIMESTAMP
        fecha_mysql = fecha.strftime("%Y-%m-%d")
        entry.delete(0, END)
        entry.insert(0, fecha_mysql)
      except ValueError:
        print("Error: Formato de fecha incorrecto")
    
    def entry(self):
        self.entry_fecha_incio = Entry(self.frame,font=('Arial', 12),relief="flat", background="white")
        self.entry_fecha_incio.place(x=300, y=100, height=25, width=150)
        self.entry_fecha_incio.bind('<FocusOut>', lambda event: self.formatear_fecha(event,self.entry_fecha_incio))

        self.entry_fecha_fin = Entry(self.frame,font=('Arial', 12),relief="flat", background="white")
        self.entry_fecha_fin.place(x=300, y=200, height=25, width=150)
        self.entry_fecha_fin.bind('<FocusOut>', lambda event: self.formatear_fecha(event,self.entry_fecha_fin))

    def obtener_fecha_inicio(self):
        return self.entry_fecha_incio.get()

    def obtener_fecha_fin(self):
        return self.entry_fecha_fin.get()

    def button(self):
        self.generar = Button(self.frame, text = "GENERAR", bg = "blue4", fg = "white", font = ("courier new", 17, "bold"), border = 5, command=self.abrir_reporte)
        self.generar.place(x=180,y=300)

    def abrir_reporte(self):
        reporte_ingresos2(self)



class App6():
    def __init__(self, master,app5_instance):
        self.frame = master
        self.app5_instance = app5_instance
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Hoyesdia21",
            database = "proyecto")
        self.cursor = self.conn.cursor()
        self.tabla_cliente()
        self.label()
        self.button()
        
    
    def cliente(self,fecha_inicio, fecha_fin):
        sql = f"""SELECT p.PedidoID, p.Gaseosa,p.Cantidad,p.Litros,d.Total FROM Pedido p
                  JOIN Detalle_factura d ON p.PedidoID = d.PedidoID
                  JOIN Cliente c ON p.PedidoID LIKE CONCAT(c.PedidoID, '%') AND DATE(c.Fecha) BETWEEN '{fecha_inicio}' AND '{fecha_fin}' """
        self.cursor.execute(sql)
        dato = self.cursor.fetchall()
        return dato    
    

    def ingreso(self,fecha_inicio, fecha_fin):
        sql = f"""SELECT SUM(d.Total) FROM Detalle_factura d
                  JOIN Pedido p ON p.PedidoID = d.PedidoID
                  JOIN Cliente c ON p.PedidoID LIKE CONCAT(c.PedidoID, '%') AND DATE(c.Fecha) BETWEEN '{fecha_inicio}' AND '{fecha_fin}' """
        self.cursor.execute(sql)
        dato = self.cursor.fetchone()[0]
        return round(dato,2)    


    def tabla_cliente(self):
        self.list_elemts = ttk.Treeview(self.frame, columns=(1, 2,3,4,5), show="headings", height= "8")

        # --- STYLE ---	
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="Royalblue4",relief="flat",foreground="white")

        
        self.list_elemts.heading(1, text="PEDIDO ID")
        self.list_elemts.heading(2, text="GASEOSA(six)")
        self.list_elemts.heading(3, text="CANTIDAD")
        self.list_elemts.heading(4, text="LITROS")
        self.list_elemts.heading(5, text="PRECIO TOTAL")
        
        self.list_elemts.column(1, anchor=CENTER, width=150)
        self.list_elemts.column(2, anchor=CENTER, width= 150)
        self.list_elemts.column(3, anchor=CENTER, width=150)
        self.list_elemts.column(4, anchor=CENTER, width= 150)
        self.list_elemts.column(5, anchor=CENTER, width=150)
        
    
        # -- LLENAR LIST--
        
        self.fecha_inicio = self.app5_instance.obtener_fecha_inicio()
        self.fecha_fin = self.app5_instance.obtener_fecha_fin()
        # Consultar la base de datos con las fechas obtenidas
        self.rows = self.cliente(self.fecha_inicio, self.fecha_fin)
        for i in self.rows:
            self.list_elemts.insert('', 'end', values=i)

        self.list_elemts.place(x=80, y=120)

        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.list_elemts.yview)
        scrollbar.place(x=835, y=120, height=190)  # Ajusta la posición y altura de la barra de desplazamiento

    # Configuración del Treeview para usar la barra de desplazamiento
        self.list_elemts.configure(yscrollcommand=scrollbar.set)

    def label(self):
        self.label_desde = Label(self.frame, foreground="black",font=("arial",14,"bold"), background="light cyan",text=f"Desde: {self.fecha_inicio}").place(x=80, y=70)
        self.label_hasta = Label(self.frame, foreground="black",font=("arial",14,"bold"), background="light cyan",text=f"Hasta: {self.fecha_fin}").place(x=400, y=70)
        
        ingreso_total = self.ingreso(self.fecha_inicio, self.fecha_fin)
        self.label_ingreso = Label(self.frame, foreground="black",font=("arial",14,"bold"), background="light cyan",text=f"Ingreso total en esa fecha: {ingreso_total}").place(x=300, y=340)


    def button(self):
        self.back = Button(self.frame, text = "ATRÁS", bg = "red3", fg = "white", font = ("courier new", 17, "bold"), border = 5, command = self.frame.destroy)
        self.back.place(x=780,y=330)


def ventana_mod():
   root = Toplevel()
   root.title("MODIFICACIÓN DE GASEOSAS")
   root.config(background="light cyan")
   root.geometry("1400x400")
   Label(root, text="INVENTARIO", fg = "black", bg = "light cyan",font = ("courier new", 28, "bold")).place(x=580, y = 20)
   App(root)
   

def reporte_gaseosa():
    root = Toplevel()
    root.title("VENTA DE GASEOSAS")
    root.config(background="light cyan")
    root.geometry("1100x650")
    Label(root, foreground="black",font=("arial",17,"bold"), background="light cyan",text="VENTA DE GASEOSAS").pack(pady = 20)
    App2(root)

def reporte_cliente():
    root = Toplevel()
    root.title("DETALLES CLIENTE")
    root.config(background="light cyan")
    root.geometry("500x400")
    Label(root, foreground="black",font=("arial",17,"bold"), background="light cyan",text="DETALLES DE CLIENTES").pack(pady = 20)
    app3_instance = App3(root)
    
   
    
def reporte_cliente_2(app3_instance):
    root = Toplevel()
    root.title("DETALLE DE CLIENTES")
    root.config(background="light cyan")
    root.geometry("1300x300")
    Label(root, foreground="black",font=("arial",19,"bold"), background="light cyan",text="DETALLES DE CLIENTES").pack(pady = 20)
    App4(root, app3_instance) 

def reporte_ingresos():
    root = Toplevel()
    root.title("DETALLES CLIENTE")
    root.config(background="light cyan")
    root.geometry("500x400")
    Label(root, foreground="black",font=("arial",17,"bold"), background="light cyan",text="DETALLES DE CLIENTES").pack(pady = 20)
    app5_instance = App5(root)
    

def reporte_ingresos2(app5_instance):
    root = Toplevel()
    root.title("INGRESOS")
    root.config(background="light cyan")
    root.geometry("900x400")
    Label(root, foreground="black",font=("arial",19,"bold"), background="light cyan",text="DETALLES DE INGRESOS").pack(pady = 20)
    App6(root, app5_instance) 

def reporte():
    root = Toplevel()
    root.title("REPORTES")
    root.config(background="light cyan")
    root.geometry("400x500")
    Button(root, text="VENTA DE GASEOSAS", font=("arial",18,"bold"),background="light grey", border = 8, command= reporte_gaseosa).place(x=50, y=70, width=300)
    Button(root, text="DETALLE CLIENTES", font=("arial",18,"bold"),background="light grey", border = 8, command= reporte_cliente).place(x=50, y=200, width=300)
    Button(root, text="INGRESOS", font=("arial",18,"bold"),background="light grey", border = 8,command= reporte_ingresos).place(x=50, y=330, width=300)






  


 








