import sqlite3

class pañol:
    def __init__(self):      
        self.conexion = sqlite3.connect("pañol8.db")
        self.cursor = self.conexion.cursor()
        self.iniciarTabla()

    def iniciarTabla(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS herramientas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT,canti INTEGER)") 
        self.conexion.commit()

    def agregarProducto(self):
        nombre = input("Ingresa el nombre: ")
        canti = int(input("Ingresa la cantidad: "))
        self.cursor.execute("INSERT INTO herramientas (nombre, canti) VALUES (?,?)", (nombre, canti))
        self.conexion.commit()

    def verProductos(self):
        self.cursor.execute("SELECT * FROM herramientas")
        productos = self.cursor.fetchall()
        for producto in productos:
            print(producto)
    
    def eliminarProducto(self):
        id = input("Ingresa el id del producto a eliminar: ")
        self.cursor.execute("DELETE FROM herramientas WHERE id = ?", (id))
        self.conexion.commit()

    def editarProducto(self):
        nombre = input("nombre: ")
        cantidad = int(input("cantidad: "))
        id = int(input("id: "))
        self.cursor.execute("UPDATE herramientas SET nombre = ?, canti = ? WHERE id = ?", (nombre, cantidad, id))
        self.conexion.commit()

Pañol = pañol()


while True:
    print("1: agregar producto, 2: ver herramientas, 3: eliminar productos, 4: editar productos, 5: salir")
    opcion = input("Que queres hacer?: ")


    if opcion == "1":
        Pañol.agregarProducto()
    elif opcion == "2":
        Pañol.verProductos()
    elif opcion == "3":
        Pañol.eliminarProducto()
    elif opcion == "4":
        Pañol.editarProducto()
    elif opcion == "5":
        break

    
