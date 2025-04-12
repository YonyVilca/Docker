from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from backend.models.mysql_libro_model import LibroModel

libro_model = LibroModel()
libro_blueprint = Blueprint('libro_blueprint', __name__)

@libro_blueprint.route('/libro', methods=['POST'])
@jwt_required()
def create_libro():
    data = request.get_json()
    required = ['titulo_libro', 'genero_id', 'autor_ids']
    if not all(k in data for k in required):
        return jsonify({"error": "Faltan datos para crear el libro"}), 400
    return jsonify(libro_model.crear_libro(data['titulo_libro'], data['genero_id'], data['autor_ids']))

@libro_blueprint.route('/libro', methods=['PUT'])
@jwt_required()
def update_libro():
    data = request.get_json()
    required = ['libro_id', 'nuevo_titulo', 'nuevo_genero_id']
    if not all(k in data for k in required):
        return jsonify({"error": "Faltan datos para actualizar el libro"}), 400
    return jsonify(libro_model.actualizar_libro(data['libro_id'], data['nuevo_titulo'], data['nuevo_genero_id']))

@libro_blueprint.route('/libro', methods=['DELETE'])
@jwt_required()
def delete_libro():
    data = request.get_json()
    if 'libro_id' not in data:
        return jsonify({"error": "libro_id es requerido"}), 400
    return jsonify(libro_model.eliminar_libro(data['libro_id']))

@libro_blueprint.route('/libro', methods=['GET'])
@jwt_required()
def get_libro():
    data = request.get_json()
    if 'libro_id' not in data:
        return jsonify({"error": "libro_id es requerido"}), 400
    return jsonify(libro_model.obtener_libro(data['libro_id']))

@libro_blueprint.route('/libros', methods=['GET'])
@jwt_required()
def get_libros():
    return jsonify(libro_model.obtener_libros())

@libro_blueprint.route('/libros/autor/<int:autor_id>', methods=['GET'])
@jwt_required()
def libros_por_autor(autor_id):
    return jsonify(libro_model.obtener_libros_por_autor(autor_id))

@libro_blueprint.route('/autores/libro/<int:libro_id>', methods=['GET'])
@jwt_required()
def autores_de_libro(libro_id):
    return jsonify(libro_model.obtener_autores_de_libro(libro_id))
