# app.py

from flask import Flask, request, jsonify
from business_logic import crear_producto, listar_todos_los_productos

app = Flask(_name_)

@app.route('/productos', methods=['POST'])
def agregar_producto_route():
    data = request.get_json()
    respuesta, status = crear_producto(data)
    return jsonify(respuesta), status

@app.route('/productos', methods=['GET'])
def listar_productos_route():
    respuesta, status = listar_todos_los_productos()
    return jsonify(respuesta), status

if _name_ == '_main_':
    app.run(debug=True)
