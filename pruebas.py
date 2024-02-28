
import mysql.connector

conn = mysql.connector.connect(
          host = "localhost",
          user = "root",
          password = "Hoyesdia21",
          database = "proyecto")

cursor = conn.cursor()

#cursor.execute("ALTER TABLE Pedido DROP FOREIGN KEY Pedido_ibfk_1")
#cursor.execute("ALTER TABLE Pedido DROP FOREIGN KEY Pedido_ibfk_2")
cursor.execute("ALTER TABLE Detalle_cliente DROP FOREIGN KEY Detalle_cliente_ibfk_1")
cursor.execute("ALTER TABLE Detalle_factura DROP FOREIGN KEY Detalle_factura_ibfk_1")

cursor.execute("DROP TABLE IF EXISTS gaseosas")
cursor.execute("DROP TABLE IF EXISTS Pedido")
cursor.execute("DROP TABLE IF EXISTS Cliente")
cursor.execute("DROP TABLE IF EXISTS Administrador")
cursor.execute("DROP TABLE IF EXISTS Detalle_cliente")
cursor.execute("DROP TABLE IF EXISTS Detalle_factura")
#tablas = ["Cliente", "Pedido", "gaseosas"]

#for tabla in tablas:
    #cursor.execute(f"DROP TABLE IF EXISTS {tabla}")

# Confirmar los cambios

conn.commit()
conn.close()