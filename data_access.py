# data_access.py

# Lista en memoria para simular la base de datos
productos = []

def agregar_producto(producto):
    productos.append(producto)

def obtener_productos():
    return productos
