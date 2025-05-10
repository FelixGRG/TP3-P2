# business_logic.py

from data_access import agregar_producto, obtener_productos

def crear_producto(data):
    if not data or 'nombre' not in data:
        return {'error': 'El producto debe tener un nombre'}, 400
    producto = {'nombre': data['nombre']}
    agregar_producto(producto)
    return {'mensaje': 'Producto agregado', 'producto': producto}, 201

def listar_todos_los_productos():
    return {'productos': obtener_productos()}, 200
