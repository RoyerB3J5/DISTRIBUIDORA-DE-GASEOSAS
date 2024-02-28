from tkinter import *
from dbpedido import *
from tkinter import messagebox
from tkinter import ttk
import databaseadmi
from resumen_server import *
from factura import*


class App:

    def __init__(self, master):
        self.frame = master
        self.DrawEntry()
        self.DrawButtons()
        self.DrawLabel()
        

    def DrawLabel(self):
        self.lbl_name = Label(self.frame, foreground="black",font=("arial",13,"bold"), background="light cyan",text="Nombre:").place(x=50, y=100)
        self.lbl_place = Label(self.frame, foreground="black",font=("arial",13,"bold"), background="light cyan", text="Dirección:").place(x=50, y=170)
        self.lbl_streat = Label(self.frame, foreground="black",font=("arial",12), background="light cyan", text="- Calle:").place(x=90, y=220)
        self.lbl_streat_num = Label(self.frame, foreground="black",font=("arial",12), background="light cyan", text="- Número:").place(x=90, y=290)
        self.lbl_mname = Label(self.frame, foreground="black",font=("arial",13,"bold"), background="light cyan", text="Nombre de Tienda:").place(x=50, y=360)
        self.lbl_ruc = Label(self.frame, foreground="black",font=("arial",13,"bold"), background="light cyan", text="RUC:").place(x=50, y=430)
        self.lbl_phone = Label(self.frame, foreground="black",font=("arial",13,"bold"), background="light cyan", text="Teléfono:").place(x=50, y=500)

    def DrawEntry(self):
        self.name = StringVar()
        self.streat = StringVar()
        self.streat_num = IntVar()
        self.mname = StringVar()
        self.ruc = StringVar()
        self.phone = IntVar()
        self.txt_name = Entry(self.frame,font=('Arial', 12),relief="flat", background="White" ,textvariable=self.name)
        self.txt_name.place(x=200, y=100, height=25, width=250)
        self.txt_streat = Entry(self.frame,font=('Arial', 12),relief="flat", background="White" ,textvariable=self.streat)
        self.txt_streat.place(x=200, y=220, height=25, width=250)
        self.txt_streat_num = Entry(self.frame,font=('Arial', 12),relief="flat", background="White" ,textvariable=self.streat_num)
        self.txt_streat_num.place(x=200, y=290, height=25, width=250)
        self.txt_mname = Entry(self.frame,font=('Arial', 12),relief="flat", background="White" ,textvariable=self.mname)
        self.txt_mname.place(x=215, y=360, height=25, width=240)
        self.txt_ruc = Entry(self.frame,font=('Arial', 12),relief="flat", background="White" ,textvariable=self.ruc)
        self.txt_ruc.place(x=200, y=430, height=25, width=250)
        self.txt_phone = Entry(self.frame,font=('Arial', 12),relief="flat", background="White" ,textvariable=self.phone)
        self.txt_phone.place(x=200, y=500, height=25, width=250)
    
    # Asocia la función convertir_a_mayusculas al evento de cambio de texto en el Entry
        self.txt_name.bind("<KeyRelease>", self.convertir_a_mayusculas)
        self.txt_streat.bind("<KeyRelease>", self.convertir_a_mayusculas)
        self.txt_mname.bind("<KeyRelease>", self.convertir_a_mayusculas)
        

    def convertir_a_mayusculas(self,event):
        # Obtiene el valor actual del Entry y lo convierte a mayúsculas
        nuevo_valor = self.txt_name.get().upper()
        self.name.set(nuevo_valor)

        nuevo_valor = self.txt_streat.get().upper()
        self.streat.set(nuevo_valor)

        nuevo_valor = self.txt_mname.get().upper()
        self.mname.set(nuevo_valor)

       
    
    def DrawButtons(self):
        
        self.btn_save = Button(self.frame,foreground="white", text="Guardar",borderwidth=2,relief="flat", cursor="hand1",overrelief="raise",background="blue4", command=self.confirmProcess).place(x=280, y=580, width=90)
        self.btn_continue = Button(self.frame,foreground="white", text="Siguiente",borderwidth=2,relief="flat", cursor="hand1",overrelief="raise",background="blue4", command=lambda:[self.frame.destroy(),ventana_ped2()]).place(x=380, y=580, width=90)
    
    def confirmProcess(self):
        if self.name.get() != "" and self.streat.get() != "" and self.streat_num.get() != "" and self.mname.get() != "" and self.ruc.get() != ""and self.phone.get() != "":
            d = Data()
            arr = [self.name.get(), self.streat.get(),self.streat_num.get(), self.mname.get(), self.ruc.get(),self.phone.get()]
            d.InsertItems(arr)
            messagebox.showinfo(title="Gracias", message="Sus datos han sido registrados, puede continuar.")
        else:
            messagebox.showinfo(title="Error", message="Debe llenar los campos para poder seguir!")	
        self.frame.focus_force()      


class App2:
    def __init__(self, master):
        self.frame = master
        self.DrawEntry()
        self.DrawList()
        self.DrawLabel()
        self.DrawRadioButtons()
        self.i = 1
      

    def DrawLabel(self):
        self.lbl_name = Label(self.frame, foreground="black",font=("arial",13,"bold"), background="light cyan",text="Gaseosa:").place(x=300, y=300)
        self.lbl_six = Label(self.frame, foreground="black",font=("arial",13,"bold"), background="light cyan", text="Cantidad:").place(x=300, y=350)
        self.lbl_liter = Label(self.frame, foreground="black",font=("arial",13,"bold"), background="light cyan", text="Litros:").place(x=300, y=400)
        self.lbl_question = Label(self.frame, foreground="black",font=("arial",13,"bold"), background="light cyan", text="Desea agregar otra gaseosa?").place(x=200, y=450)
        


    def DrawEntry(self):
        self.name = StringVar()
        self.six = IntVar()
        self.liter = StringVar()
        self.txt_name = Entry(self.frame,font=('Arial', 12),relief="flat", background="CadetBlue2" ,textvariable=self.name)
        self.txt_name.place(x=400, y=300, height=25, width=150)
        self.txt_six= Entry(self.frame,font=('Arial', 12),relief="flat", background="CadetBlue2" ,textvariable=self.six)
        self.txt_six.place(x=400, y=350, height=25, width=150)
        self.txt_liter= Entry(self.frame,font=('Arial', 12),relief="flat", background="CadetBlue2" ,textvariable=self.liter)
        self.txt_liter.place(x=400, y=400, height=25, width=150)

        # Asocia la función convertir_a_mayusculas al evento de cambio de texto en el Entry
        self.txt_name.bind("<KeyRelease>", self.convertir_a_mayusculas)
        
        

    def convertir_a_mayusculas(self,event):
        # Obtiene el valor actual del Entry y lo convierte a mayúsculas
        nuevo_valor = self.txt_name.get().upper()
        self.name.set(nuevo_valor)
        

        
    
    def DrawRadioButtons(self):
        self.opcion = IntVar()
        self.yes = Radiobutton(self.frame, text = "Si",font=('Arial', 12), bg = "light cyan",variable= self.opcion, value = 1, command=self.Save). place(x= 340, y = 490)
        self.no = Radiobutton(self.frame, text = "No",font=('Arial', 12), bg = "light cyan", variable= self.opcion, value = 2,command = self.Save). place(x= 540, y = 490)
    
    def ClearEntry(self):
        self.name.set("")
        self.six.set("")
        self.liter.set("")

   

    def confirmProcess2(self):
        
        if self.name.get() != "" and self.six.get() != ""and self.liter.get() != "":
            d = Data2()
            arr = [self.name.get(), self.six.get(),self.liter.get()]
            d.InsertItems2(arr,self.i)
            d.UpdateSix(self.liter.get(),self.six.get(),self.name.get())
            #d.InsertCost()
    

    def Save(self):
        if self.opcion.get() == 1 :
            self.confirmProcess2()
            self.i+=1
            self.DrawList()
            self.ClearEntry()
            self.DrawLabel()
            self.ClearEntry()
            self.DrawRadioButtons()
        elif self.opcion.get() == 2 :
            self.confirmProcess2()
            self.i=1
            self.DrawList()
            self.frame.destroy()
            ventana_ped3()
            

    def DrawList(self):
        self.list_elemts = ttk.Treeview(self.frame, columns=(1, 2, 3, 4), show="headings", height="8")

        # --- STYLE ---	
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="Royalblue4",relief="flat",foreground="white")
        #style.map("Treeview", background=[('selected', 'yellow')], foreground=[('selected', 'black')])

        self.list_elemts.heading(1, text="Nombre")
        self.list_elemts.heading(2, text="Cantidad(six pack)")
        self.list_elemts.heading(3, text="Precio")
        self.list_elemts.heading(4, text="Capacidad (L)")
        self.list_elemts.column(1, anchor=CENTER)
        self.list_elemts.column(2, anchor=CENTER)
        self.list_elemts.column(3, anchor=CENTER)
        self.list_elemts.column(4, anchor=CENTER)

        # -- LLENAR LIST--
        d = Data2()
        self.rows = d.returnAllElements()
        for i in self.rows:
            self.list_elemts.insert('', 'end', values=i)
        # ----- fin -----
        self.list_elemts.place(x=50, y=80)
        scrollbar = ttk.Scrollbar(self.frame, orient="vertical", command=self.list_elemts.yview)
        scrollbar.place(x=850, y=80, height=190)  # Ajusta la posición y altura de la barra de desplazamiento

    # Configuración del Treeview para usar la barra de desplazamiento
        self.list_elemts.configure(yscrollcommand=scrollbar.set)
  
    
def ventana_ped3():
    root = Toplevel()
    root.title("REALIZAR PEDIDO")
    root.config(background="light cyan")


    root.grid_columnconfigure(0, weight=1)

    lbl_tittle = Label(root, text="RESUMEN DE PEDIDO", fg = "black", bg = "light cyan",font = ("courier new", 20, "bold"))
    lbl_tittle.grid(row=0, column=0,columnspan=5, sticky="nsew",pady=(20, 0))
    for col in range(5):
        root.grid_columnconfigure(col, weight=1)
    spacer = Label(root, text="", bg="light cyan")
    spacer.grid(row=1, column=0)
    lbl_name = Label(root, foreground="black", font=("arial", 13, "bold"), background="light cyan", text="Gaseosa").grid(row=2, column=0, sticky="nsew")
    lbl_six = Label(root, foreground="black", font=("arial", 13, "bold"), background="light cyan", text="Cantidad").grid(row=2, column=1, sticky="nsew")
    lbl_liter = Label(root, foreground="black", font=("arial", 13, "bold"), background="light cyan", text="Capacidad(L)").grid(row=2, column=2, sticky="nsew")
    lbl_price = Label(root, foreground="black", font=("arial", 13, "bold"), background="light cyan", text="Precio (u)").grid(row=2, column=3, sticky="nsew")
    lbl_pricet = Label(root, foreground="black", font=("arial", 13, "bold"), background="light cyan", text="Precio Total (s/.)").grid(row=2, column=4, sticky="nsew")
    spacer = Label(root, text="", bg="light cyan")
    spacer.grid(row=3, column=0)
    d = Data2()
    order = d.resumen()
    
    row_position = 4

    for i in order:
        col_position = 0
        for j in i[1:]:
            lbl_order = Label(root, foreground="black", font=("arial", 12), background="light cyan", text=j).grid(row=row_position, column=col_position, sticky="nsew")
            spacer = Label(root, text="", bg="light cyan")
            spacer.grid(row=row_position+1, column=0)
            col_position += 1

        row_position += 2
    
    subtotal = d.Subtotal() 
    val_subtotal = 0

    row_position_1 = 4
    
    for i in subtotal:
        for j in i:
            lbl_order = Label(root, foreground="black", font=("arial", 12), background="light cyan", text=j).grid(row=row_position_1, column=4, sticky="nsew")
            spacer = Label(root, text="", bg="light cyan")
            spacer.grid(row=row_position+1, column=0)
            val_subtotal+= j
        row_position_1 += 2
    

    spacer = Label(root, text="", bg="light cyan")
    spacer.grid(row=row_position, column=0)
    lbl_line = Label(root, foreground="black", font=("arial", 13), background="light cyan", text="-----------------").grid(row=row_position, column=4, sticky="s")

    lbl_subtotal = Label(root, foreground="black", font=("arial", 13, "bold"), background="light cyan", text="SubTotal:").grid(row=row_position+1, column=3, sticky="e")
    lbl_pay = Label(root, foreground="black", font=("arial", 13, "bold"), background="light cyan", text=val_subtotal).grid(row=row_position+1, column=4, sticky="nsew")

    igv = d.igv()
    lbl_igv = Label(root, foreground="black", font=("arial", 13), background="light cyan", text="IGV (18%):").grid(row=row_position+2, column=3, sticky="e")
    lbl_igv_value = Label(root, foreground="black", font=("arial", 13), background="light cyan", text=igv).grid(row=row_position+2, column=4, sticky="nsew")

    total = d.Total()
    lbl_total = Label(root, foreground="black", font=("arial", 13, "bold"), background="light cyan", text="Pago Total:").grid(row=row_position+3, column=3, sticky="e")
    lbl_total_value = Label(root, foreground="black", font=("arial", 13, "bold"), background="light cyan", text=total).grid(row=row_position+3, column=4, sticky="nsew")

    spacer = Label(root, text="", bg="light cyan")
    spacer.grid(row=row_position+4, column=0)
    spacer = Label(root, text="", bg="light cyan")
    spacer.grid(row=row_position+5, column=0)
    button_save = Button(root, foreground="white", text="CONFIRMAR PEDIDO", borderwidth=2, relief="flat", cursor="hand1", overrelief="raise", background="SeaGreen3",width=17, height=1, command= lambda:[root.destroy(),factura()]).grid(row=row_position+6, column=4)

    y = row_position*60
    root.geometry(f"1100x{y}")
    
    

def ventana_ped2():
    root = Toplevel()
    root.title("REALIZAR PEDIDO")
    root.config(background="light cyan")
    root.geometry("900x550")
    Label(root, text="Pedido:", fg = "black", bg = "light cyan",font = ("courier new", 20, "bold")).place(x=30, y = 30)
    App2(root)
   
   
    


def ventana_ped():
  root = Toplevel()
  root.title("REALIZAR PEDIDO")
  root.config(background="light cyan")
  root.geometry("500x650")
  Label(root, text="Ingrese sus datos", fg = "black", bg = "light cyan",font = ("courier new", 20, "bold")).place(x=30, y = 30)
  App(root)



  



  
