import mysql.connector

class Data:

    def __init__(self):
        self.conn = mysql.connector.connect(
          host = "localhost",
          user = "root",
          password = "Hoyesdia21",
          database = "proyecto")

        self.cursor = self.conn.cursor()


    
    def InsertItems(self, element):
        
        sql = "insert into Cliente(Nombre, NombreTienda, Ruc, Telefono) values('{}', '{}', '{}','{}')".format(element[0],element[3],element[4],element[5])
        self.cursor.execute(sql)
        self.cursor.execute("SELECT PedidoID FROM Cliente ORDER BY PedidoID DESC LIMIT 1")
        pedido_id = self.cursor.fetchone()[0]
        sql = "insert into Detalle_cliente(PedidoID,Calle, Numero) values('{}', '{}','{}')".format(pedido_id,element[1],element[2])
        self.cursor.execute(sql)
        self.conn.commit()

    def ReturnElements(self):
        sql = "SELECT * FROM Cliente ORDER BY PedidoID DESC LIMIT 1"
        self.cursor.execute(sql)
        element = self.cursor.fetchone()
        return element
        
class Data2:

    def __init__(self):
        self.conn = mysql.connector.connect(
          host = "localhost",
          user = "root",
          password = "Hoyesdia21",
          database = "proyecto")

        self.cursor = self.conn.cursor()
    
    def InsertItems2(self, element,i):
        self.cursor.execute("SELECT PedidoID FROM Cliente ORDER BY PedidoID DESC LIMIT 1")
        pedido_id = self.cursor.fetchone()[0]
        codigo_ped = f"{pedido_id}.{i}"
        sql = "insert into Pedido(PedidoID,Gaseosa,Cantidad, Litros) values('{}','{}', '{}','{}')".format(codigo_ped,element[0],element[1], element[2])
        self.cursor.execute(sql)
        update_sql = f"""UPDATE Pedido SET Costo = (SELECT Precio FROM gaseosas WHERE gaseosas.Nombre = UPPER(Pedido.Gaseosa) 
                         AND gaseosas.Litros = Pedido.Litros) WHERE PedidoID = '{codigo_ped}'"""
        self.cursor.execute(update_sql)
        update_id = f"UPDATE Pedido SET ClienteId = '{pedido_id}' WHERE PedidoID LIKE '{pedido_id}%'"
        self.cursor.execute(update_id)
        self.conn.commit()
    
    def returnAllElements(self):
        sql = "select Nombre, SixPack,Precio, Litros from gaseosas"
        self.cursor.execute(sql)
        return self.cursor.fetchall()
    
    def InsertCost(self):
        sql = "UPDATE Pedido SET Costo = (SELECT Precio FROM gaseosas WHERE Pedido.Gaseosa = gaseosas.Nombre AND Pedido.Litros = gaseosas.Litros) "
        self.cursor.execute(sql)
        self.conn.commit()

    def UpdateSix(self, litro,six,Nombre):
        self.cursor.execute(f"SELECT SixPack FROM gaseosas WHERE Litros = '{litro}'AND Nombre = '{Nombre}'")    
        resultado = self.cursor.fetchone()  
        valor_columna = resultado[0] if resultado else None
        valor = int(valor_columna)
        resultado = valor - six
        self.cursor.execute(f"UPDATE gaseosas SET SixPack = '{resultado}' WHERE Litros = '{litro}'AND Nombre = '{Nombre}'")
        self.conn.commit()

    def resumen(self):
        self.cursor.execute("SELECT PedidoID FROM Cliente ORDER BY PedidoID DESC LIMIT 1")
        pedido_id = self.cursor.fetchone()[0]
        sql = f"SELECT * FROM Pedido WHERE PedidoId LIKE'{pedido_id}%'"
        self.cursor.execute(sql)
        result =self.cursor.fetchall()
        return result
    
    def Subtotal(self):
        self.cursor.execute("SELECT PedidoID FROM Cliente ORDER BY PedidoID DESC LIMIT 1")
        pedido_id = self.cursor.fetchone()[0]
        sql = f"SELECT Subtotal FROM Detalle_Factura WHERE PedidoId LIKE'{pedido_id}%'"
        self.cursor.execute(sql)
        result =self.cursor.fetchall()
        return result
    
    
    def igv(self):
        self.cursor.execute("SELECT PedidoID FROM Cliente ORDER BY PedidoID DESC LIMIT 1")
        pedido_id = self.cursor.fetchone()[0]
        sql = f"SELECT Igv FROM Detalle_Factura WHERE PedidoId LIKE'{pedido_id}%'"
        self.cursor.execute(sql)
        result =self.cursor.fetchall()
        val = 0
        for i in result:
            for j in i:
                val+=j
        return round(val,2)
    
    def Total(self):
        self.cursor.execute("SELECT PedidoID FROM Cliente ORDER BY PedidoID DESC LIMIT 1")
        pedido_id = self.cursor.fetchone()[0]
        sql = f"SELECT Total FROM Detalle_Factura WHERE PedidoId LIKE'{pedido_id}%'"
        self.cursor.execute(sql)
        result =self.cursor.fetchall()
        val = 0
        for i in result:
            for j in i:
                val+=j
        return val
    
    def direccion(self):
        self.cursor.execute("SELECT Calle, Numero FROM Detalle_cliente ORDER BY PedidoID DESC LIMIT 1")
        result =self.cursor.fetchone()
        return result
    
    def fecha(self):
        self.cursor.execute("SELECT Fecha FROM Cliente ORDER BY PedidoID DESC LIMIT 1")
        result =self.cursor.fetchone()[0]
        return result
    
    def factura(self):
        self.cursor.execute("SELECT PedidoID FROM Cliente ORDER BY PedidoID DESC LIMIT 1")
        pedido_id = self.cursor.fetchone()[0]
        sql = f"SELECT Gaseosa,Cantidad,Litros, Costo FROM Pedido WHERE PedidoId LIKE'{pedido_id}%'"
        self.cursor.execute(sql)
        result =self.cursor.fetchall()
        return result
        
        
        

    





    
    

    



        
   
    
        

