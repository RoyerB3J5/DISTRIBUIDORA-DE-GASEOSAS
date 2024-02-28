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
		
		sql = "insert into gaseosas(Nombre, SixPack, Precio, Litros) values('{}', '{}', '{}','{}')".format(element[0],element[1],element[2], element[3])
		
		self.cursor.execute(sql)
		self.conn.commit()


	
	def ReturnOneItem(self, ref):
		
		sql = "select * from gaseosas where Nombre = '{}'".format(ref)
		self.cursor.execute(sql)
		
		return self.cursor.fetchone()


	def returnAllElements(self):
		sql = "select * from gaseosas"
		self.cursor.execute(sql)
		return self.cursor.fetchall()


	def Delete(self, ref,ref1):
		sql = "delete from gaseosas where Nombre = '{}' AND Precio = '{}'".format(ref,ref1)
		self.cursor.execute(sql)
		self.conn.commit()

    
	def UpdateItem(self, element, ref):
    
		sql = "UPDATE gaseosas SET Nombre = %s, SixPack = %s, Precio = %s, Litros = %s WHERE Codigo = %s"
    
    
		self.cursor.execute(sql, (element[1], element[2], element[3], element[4], ref))
    
    
		self.conn.commit()

	
		
class Data_1admi():
	def __init__(self):
		self.conn = mysql.connector.connect(
          host = "localhost",
          user = "root",
          password = "Hoyesdia21",
          database = "proyecto")

		self.cursor = self.conn.cursor()

	def circulo(self):
		sql = "SELECT Gaseosa, SUM(Cantidad) FROM Pedido GROUP BY Gaseosa"
		self.cursor.execute(sql)
		dato = self.cursor.fetchall()
		return dato
	
	def total(self):
		sql = "SELECT SUM(Cantidad) FROM Pedido "
		self.cursor.execute(sql)
		dato = self.cursor.fetchone()[0]
		return dato

	def max_gaseosa(self):
		sql = "SELECT Gaseosa FROM Pedido GROUP BY Gaseosa ORDER BY SUM(Cantidad) DESC LIMIT 1 "
		self.cursor.execute(sql)
		dato = self.cursor.fetchone()[0]
		return dato



		