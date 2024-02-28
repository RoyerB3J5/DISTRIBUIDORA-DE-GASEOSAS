import mysql.connector
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Hoyesdia21",
    database = "proyecto"
)

cursor = conexion.cursor()
#   cursor.execute("SHOW DATABASES")
cursor.execute("DROP TABLE IF EXISTS gaseosas")

cursor.execute("CREATE TABLE gaseosas(Codigo INT AUTO_INCREMENT PRIMARY KEY , Nombre VARCHAR(255) , SixPack INT, Precio FLOAT, Litros DOUBLE,INDEX idx_nombre (Nombre)) AUTO_INCREMENT = 10010 ") 
valores = [
    ("COCACOLA", 20, 13.5,0.5),
    ("GUARANA", 25, 10, 0.45),
    ("PEPSI", 30, 11.50, 0.5),
    ("INKACOLA",48, 14, 0.5),
    ("KR", 35, 7.5, 0.35)
]

cursor.executemany("INSERT INTO gaseosas (Nombre, SixPack, Precio, Litros) VALUES (%s,%s,%s, %s)", valores)

cursor.execute("CREATE TABLE Cliente( PedidoID INT AUTO_INCREMENT PRIMARY KEY, Nombre VARCHAR(255), NombreTienda VARCHAR(255), Ruc BIGINT, Telefono BIGINT, Fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
cursor.execute("CREATE TABLE Pedido( PedidoID VARCHAR(30), Gaseosa VARCHAR(255), Cantidad INT, Litros DOUBLE, Costo FLOAT, INDEX idx_pedidoid (PedidoID),FOREIGN KEY (Gaseosa) REFERENCES gaseosas(Nombre))")
cursor.execute("CREATE TABLE Administrador( id_usuario INT AUTO_INCREMENT PRIMARY KEY, Usuario BIGINT, Clave VARCHAR(255))")
cursor.execute("CREATE TABLE Detalle_cliente(PedidoID INT UNIQUE, Calle VARCHAR(50), Numero INT, FOREIGN KEY (PedidoId) REFERENCES Cliente(PedidoId))")
cursor.execute("CREATE TABLE Detalle_factura ( PedidoID VARCHAR(30) , Subtotal FLOAT, Igv FLOAT GENERATED ALWAYS AS (Subtotal*0.18) VIRTUAL,Total FLOAT GENERATED ALWAYS AS (Subtotal + Igv) VIRTUAL, FOREIGN KEY (PedidoID) REFERENCES Pedido(PedidoID))")
cursor.execute("INSERT INTO Administrador (Usuario,Clave) VALUES (10001, 'MECATRONICA')")

conexion.commit()
cursor.execute("SHOW TABLES")
for dato in cursor:
    print(dato)

conexion.commit()
conexion.close()