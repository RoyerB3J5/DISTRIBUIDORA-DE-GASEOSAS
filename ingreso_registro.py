from tkinter import *
from principaladmi import *

def seguridad_admi():
    
    pagina2 =Toplevel()
    pagina2.title("USUARIO DE ADMINISTRADOR")
    pagina2.geometry("600x400")
    pagina2.config(bg="light cyan")
    Label(pagina2, text="INGRESE USUARIO DE ADMINISTRADOR",fg = "black", bg = "light cyan" ,font=("courier new", 20, "bold")).place(x=40,y=30)
    Label(pagina2, text="USUARIO:",fg = "black", bg = "light cyan" ,font=("courier new", 14, "bold")).place(x=120,y=120)
    Label(pagina2, text="CONTRASEÑA:",fg = "black", bg = "light cyan" ,font=("courier new", 14, "bold")).place(x=120,y=200)
    
    user_val = StringVar()
    key_val = StringVar()

    Entry(pagina2,font=('Arial', 12),relief="flat", background="white" ,textvariable=user_val).place(x=260, y=120, height=25, width=150)
    Entry(pagina2,font=('Arial', 12),relief="flat", background="white" ,textvariable=key_val, show="*").place(x=260, y=200, height=25, width=150)
    
       
     
    
    def signin(usuario, clave):
      conn = mysql.connector.connect(
          host = "localhost",
          user = "root",
          password = "Hoyesdia21",
          database = "proyecto")

      cursor = conn.cursor()

      query = "SELECT * FROM administrador WHERE Usuario = %s AND Clave = %s"
      cursor.execute(query, (usuario, clave))
      result = cursor.fetchone()

      cursor.close()
      conn.close()

      if result:
        return True
      else:
        return False
      
    def verificacion():
       usuario = user_val.get()
       clave = key_val.get()

       if signin(usuario, clave):
         administrador()
         pagina2.destroy()
       else:
         messagebox.showwarning(title="USUADIO DE ADMINISTRADOR", message= "Usuario y/o contraseña incorrecto")

    Button(pagina2, text = "INGRESAR", bg = "light grey", font = ("courier new", 20, "bold"), border = 5, command=verificacion).place(x=130, y=300)
    Button(pagina2, text = "REGISTRAR", bg = "light grey", font = ("courier new", 20, "bold"), border = 5,command=login).place(x=330, y=300)

         
def login():
      
      pagina4 = Toplevel()
      pagina4.title("REGISTRO")
      pagina4.geometry("450x400")
      pagina4.config(bg="light cyan")
      Label(pagina4, text="REGISTRAR NUEVO USUARIO",fg = "black", bg = "light cyan" ,font=("courier new", 20, "bold")).place(x=40,y=30)
      Label(pagina4, text="NUEVO USUARIO:",fg = "black", bg = "light cyan" ,font=("courier new", 14, "bold")).place(x=50,y=120)
      Label(pagina4, text="NUEVA CONTRASEÑA:",fg = "black", bg = "light cyan" ,font=("courier new", 14, "bold")).place(x=50,y=200)
      
      global new_user
      global new_key
      new_user = StringVar()
      new_key = StringVar()

      Entry(pagina4,font=('Arial', 12),relief="flat", background="white" ,textvariable=new_user).place(x=250, y=120, height=25, width=150)
      Entry(pagina4,font=('Arial', 12),relief="flat", background="white" ,textvariable=new_key).place(x=250, y=200, height=25, width=150)
      
      

      def confirmacion_login():
       pagina5 = Toplevel()
       pagina5.title("REGISTRO")
       pagina5.geometry("450x300")
       pagina5.config(bg="light cyan")
       Label(pagina5, text="CONFIRMACION DE REGISTRO",fg = "black", bg = "light cyan" ,font=("courier new", 20, "bold")).place(x=30,y=30)
       Label(pagina5, text="CONTRASEÑA PRINCIPAL:",fg = "black", bg = "light cyan" ,font=("courier new", 14, "bold")).place(x=20,y=90)
       
       global confirm_key
       confirm_key = StringVar()

       Entry(pagina5,font=('Arial', 12),relief="flat", background="white" ,textvariable=confirm_key, show = "*").place(x=120, y=150, height=25, width=200)
       Button(pagina5, text = "CONFIRMAR REGISTRO", bg = "light grey", font = ("courier new", 20, "bold"), border = 4, command= lambda:[pagina5.destroy(),verificar_e_insertar()]).place(x=60, y=220,height=40, width=325)

      def verificar_clave(clave):
       conn = mysql.connector.connect(
          host = "localhost",
          user = "root",
          password = "Hoyesdia21",
          database = "proyecto")
       cursor = conn.cursor()

       query = "SELECT Clave FROM Administrador"
       cursor.execute(query)
       result = cursor.fetchone()

       

       if result and result[0] == clave:
         
         conn.close()
         return True
       else:
         
         conn.close()
         return False
       
      def insertar_usuario(usuario, clave):
        conn = mysql.connector.connect(
          host = "localhost",
          user = "root",
          password = "Hoyesdia21",
          database = "proyecto")
        cursor = conn.cursor()

        cursor = conn.cursor()

        query = "INSERT INTO Administrador (Usuario, Clave) VALUES (%s, %s)"
        cursor.execute(query, (usuario, clave))
        conn.commit()
        cursor.close()
        conn.close()

      def verificar_e_insertar():
          clave_ingresada = confirm_key.get()
          if verificar_clave(clave_ingresada):
            usuario = new_user.get()
            contraseña = new_key.get()
            insertar_usuario(usuario, contraseña)
            messagebox.showinfo("Éxito", "Usuario y contraseña insertados correctamente.")
            
          else:
            messagebox.showerror("Error", "La clave ingresada no coincide.")
      
      Button(pagina4, text = "REGISTRAR", bg = "light grey", font = ("courier new", 20, "bold"), border = 4, command=lambda:[pagina4.destroy(),confirmacion_login()]).place(x=130, y=300)
      
def mostrar_reporte():
       reporte()  

def administrador ():
      
      pagina3 = Toplevel()
      pagina3.title("ADMINISTRACION")
      pagina3.geometry("400x400")
      pagina3.config(bg="light cyan")
     #Elaboracion de los botones
      modificar = Button(pagina3, text = "MODIFICAR PRODUCTO", bg = "light grey", font = ("courier new", 20, "bold"), border = 5, command= ventana_mod)
      modificar.place(x=50, y=70)
      reporte = Button(pagina3, text = "MOSTRAR REPORTE", bg = "light grey", font = ("courier new", 20, "bold"), border = 5,command = mostrar_reporte)
      reporte.place(x=70, y=200)
      back= Button(pagina3, text = "ATRÁS", bg = "red3", fg = "white", font = ("courier new", 20, "bold"), border = 5, command = pagina3.destroy)
      back.place(x=250,y=300)

