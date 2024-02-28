from tkinter import *
from dbpedido import *
from tkinter import ttk
from resumen_server import *
from datetime import datetime

def factura():
    root = Toplevel()
    root.title("FACTURA")
    root.config(background="white")

    d = Data()
    d_2 = Data2()

    lbl_tittle = Label(root, text="FACTURA", fg = "black", bg = "white",font = ("courier new", 14)).pack(pady=10)
    lbl_tittle2 = Label(root, text="DISTRIBUIDORA DE GASEOSAS", fg = "black", bg = "white",font = ("courier new", 22, "bold")).pack()
    gaseosa_ruc = Label(root, text="RUC: 45236548719", fg = "black", bg = "white",font = ("courier new", 12, "bold")).place(x=900, y = 55)

    fecha_label = Label(root, text="", font=("Arial", 8), bg="white")
    fecha_label.place(x=900, y=15)
    fecha = d_2.fecha()
    fecha_label.config(text=f"Fecha y Hora: {fecha}")


    cliente_name = Label(root, text="Nombre: ", fg = "black", bg = "white",font = ("courier new", 18, "bold")).place(x=30, y = 100)
    cliente_mname = Label(root, text="Nombre de Tienda:", fg = "black", bg = "white",font = ("courier new", 18, "bold")).place(x=30, y = 130)
    cliente_ruc = Label(root, text="RUC:", fg = "black", bg = "white",font = ("courier new", 18, "bold")).place(x=30, y = 160)
    cliente_phone = Label(root, text="Teléfono:", fg = "black", bg = "white",font = ("courier new", 18, "bold")).place(x=30, y = 190)
    cliente_place = Label(root, text="Dirección: ", fg = "black", bg = "white",font = ("courier new", 18, "bold")).place(x=30, y = 220)


    global imagen
    imagen = PhotoImage(file="gaseosas2.png")
    lbl_imagen = Label(root, image=imagen, bg = "white")
    lbl_imagen.place(x =850,y =150) 

    
    cliente = d.ReturnElements()
    n_factura = Label(root, text="#Factura: ", fg = "black", bg = "white",font = ("courier new", 16, "bold")).place(x=820, y = 100) 
    valor_factura =Label(root, text=cliente[0], fg = "black", bg = "white",font = ("courier new", 16)).place(x=980, y = 100)

    d_y = 100
    for i in cliente[1:5]:
        cliente_dato = Label(root, text=i, fg = "black", bg = "white",font = ("courier new", 16 )).place(x=300, y = d_y)
        d_y += 30


    direccion = d_2.direccion()
    d_x = 300
    for i in direccion:
        cliente_direccion = Label(root, text=i, fg = "black", bg = "white",font = ("courier new", 16 )).place(x=d_x, y = 220)
        d_x += 180



    list_elemts = ttk.Treeview(root, columns=(1, 2, 3, 4,5), show="headings", height="8")

            # --- STYLE ---	
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="black",relief="flat",foreground="white", font = ("courier new",12, "bold"))

    list_elemts.heading(1, text="GASEOSA")
    list_elemts.heading(2, text="CANTIDAD(six pack)")
    list_elemts.heading(3, text="CAPACIDAD(L)")
    list_elemts.heading(4, text="PRECIO(u)")
    list_elemts.heading(5, text="PRECIO")
    list_elemts.column(1, anchor=CENTER)
    list_elemts.column(2, anchor=CENTER)
    list_elemts.column(3, anchor=CENTER)
    list_elemts.column(4, anchor=CENTER)
    list_elemts.column(5, anchor=CENTER)


    rows = d_2.factura()
    for i in rows:
        list_elemts.insert('', 'end', values=i)

    subtotal = d_2.Subtotal()
    subtotal_val=0
    filas = list_elemts.get_children()

    for fila, valores in zip(filas, subtotal):
    # Obtener el valor de la última columna
       valor_columna_5 = valores[-1]
    # Insertar el valor en la última columna de la fila correspondiente
       list_elemts.item(fila, values=[*list_elemts.item(fila)['values'][:4], valor_columna_5])
    # Calcular el subtotal
       subtotal_val += valor_columna_5
    
         
    

    num_rows = len(list_elemts.get_children())
    list_elemts["height"] = num_rows
    list_elemts.pack()
    list_elemts.place(x=50, y=300)

    lbl_subtotal = Label(root, foreground="black", font=("arial", 13, "bold"), background="white", text="SubTotal:").place(x=850, y = 330+50*num_rows)
    lbl_subtotal_val = Label(root, foreground="black", font=("arial", 13, "bold"), background="white", text=subtotal_val).place(x=950, y = 330+50*num_rows)

    lbl_igv = Label(root, foreground="black", font=("arial", 13, "bold"), background="white", text="IGV(18%):").place(x=850, y = 370+50*num_rows)
    igv = d_2.igv()
    lbl_igv_val = Label(root, foreground="black", font=("arial", 13, "bold"), background="white", text=igv).place(x=950, y = 370+50*num_rows)

    lbl_total = Label(root, foreground="black", font=("arial", 13, "bold"), background="white", text="Pago Total:").place(x=850, y = 410+50*num_rows)
    total = d_2.Total()
    lbl_total_val = Label(root, foreground="black", font=("arial", 13, "bold"), background="white", text=total).place(x=950, y = 410+50*num_rows)

    lbl_thank = Label(root, foreground="black", font=("arial", 9, "italic"), background="white", text="Gracias por su compra!!!").pack(side="bottom", pady=10, anchor="s")
    y = 400+num_rows*100
    root.geometry(f"1100x{y}")
  


    



    




    




