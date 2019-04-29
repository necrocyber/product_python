# Project Python by Antonio Medel @2019

# Importamos Librerias GUI
from tkinter import ttk
from tkinter import *

# Importamos Libreria DataBase Sqlite
import sqlite3

# Clase producto
class Product:
    # Nuestra base de datos local
    db_name = 'database.db'
    # Nuestro Constructor
    def __init__(self, window):
        self.wind = window
        self.wind.title("Application System")

        # Creando un Frame Container
        frame = LabelFrame(self.wind, text = "Registra un nuevo producto")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # Input Nombre
        Label(frame, text = "Nombre: ").grid(row = 1, column = 0)
        self.inputname = Entry(frame)
        self.inputname.grid(row = 1, column = 1)
        self.inputname.focus()

        # Input Precio
        Label(frame, text = "Precio: ").grid(row = 2, column = 0)
        self.inputprecio = Entry(frame)
        self.inputprecio.grid(row = 2, column = 1)

        # Boton Agregar Productos
        Button(frame, text = "Guardar Producto", command = self.add_product).grid(row = 3, columnspan = 2, sticky = W + E)

        # Tabla
        self.tree = ttk.Treeview(height = 10, columns = 2)
        self.tree.grid(row = 4, column = 0, columnspan = 2)
        self.tree.heading('#0', text = "Nombre", anchor = CENTER)
        self.tree.heading('#1', text = "Precio", anchor = CENTER)

        self.get_product()

    def sqlite(self, query, params = ()):
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            result = cursor.execute(query, params)
            conn.commit()
        return result

    def get_product(self):
        # Eliminando los registros en la tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        query = 'SELECT * FROM productos ORDER BY nombre ASC'
        get_rows = self.sqlite(query)
        for item in get_rows:
            self.tree.insert('', 0, text = item[1], values = item[2])

    def add_product(self):
        query = 'INSERT INTO productos (nombre, precio) VALUES (?,?)'
        insert_row = self.sqlite(query, ( self.inputname.get(), self.inputprecio.get()) )
        print(insert_row)
        self.tree.insert('', 0, text = self.inputname.get(), values = self.inputprecio.get())
        self.inputname.delete(0, END)
        self.inputprecio.delete(0, END)
        # Esta función nos sirve para crear una ventana nueva sobre la actual
        # Toplevel() Crea ventana
        # Destroy() Cierra ventana 

# Verificamos si este es nuestro archivo principal
if __name__ == '__main__':
    window = Tk()
    Application = Product(window)
    window.mainloop()





