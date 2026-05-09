import sqlite3

class pañol:
    def __init__(self):      
        self.conexion = sqlite3.connect("pañol.db")
        self.cursor = self.conexion.cursor()
        self.iniciarTabla()

    def iniciarTabla(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS herramientas (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT,canti INTEGER)") 
        self.conexion.commit()

    def agregarProducto(self, nombre: str, canti: int):
        self.cursor.execute("INSERT INTO herramientas (nombre, canti) VALUES (?,?)", (nombre, canti))
        self.conexion.commit()

    def verProductos(self):
        self.cursor.execute("SELECT * FROM herramientas")
        productos = self.cursor.fetchall()
        for producto in productos:
            print(producto)
    
    def eliminarProducto(self, id: int):
        self.cursor.execute("DELETE FROM herramientas WHERE id = ?", (id,))
        self.conexion.commit()

    def editarProducto(self, nombre: str, cantidad: int, id: int):
        self.cursor.execute("UPDATE herramientas SET nombre = ?, canti = ? WHERE id = ?", (nombre, cantidad, id))
        self.conexion.commit()

Pañol = pañol()


while True:
    print("Pañol de la técnica")
    print()
    print("[1]: Agregar herramienta")
    print("[2]: Ver herramientas")
    print("[3]: Eliminar herramienta")
    print("[4]: Editar herramienta")
    print("[5]: Salir de la DB")
    print()
    opcion = int(input("Ingrese la acción a realizar: "))


    if opcion == 1:
        Pañol.agregarProducto(input("Nombre: "), int(input("Cantidad: ")))
    elif opcion == 2:
        Pañol.verProductos()
    elif opcion == 3:
        Pañol.eliminarProducto(int(input("ID: ")))
    elif opcion == 4:
        Pañol.editarProducto(input("Nombre: "), int(input("Cantidad: ")), int(input("ID: ")))
    elif opcion == 5:
        break
