import mysql.connector
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Hoyesdia21",
    database = "proyecto"
)

cursor = conexion.cursor()

def subtotal():
        cursor.execute("SELECT PedidoID FROM Cliente ORDER BY PedidoID DESC LIMIT 1")
        pedido_id = cursor.fetchone()[0]
        sql = f"SELECT Costo_t FROM Detalle_factura WHERE PedidoId = '{pedido_id}'"
        cursor.execute(sql)
        result =cursor.fetchall()
        pago = 0
        for i in result:
                for j in i:
                        pago += j         
        return pago
                
