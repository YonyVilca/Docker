from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from backend.models.mysql_autor_model import AutorModel

autor_model = AutorModel()
autor_blueprint = Blueprint('autor_blueprint', __name__)

@autor_blueprint.route('/autor', methods=['POST'])
@jwt_required()
def create_autor():
    data = request.get_json()
    if not data or 'nombre_autor' not in data:
        return jsonify({"error": "nombre_autor es requerido"}), 400
    content = autor_model.crear_autor(data['nombre_autor'])
    return jsonify(content)

@autor_blueprint.route('/autor', methods=['PUT'])
@jwt_required()
def update_autor():
    data = request.get_json()
    if not data or 'autor_id' not in data or 'nuevo_nombre' not in data:
        return jsonify({"error": "autor_id y nuevo_nombre son requeridos"}), 400
    content = autor_model.actualizar_autor(data['autor_id'], data['nuevo_nombre'])
    return jsonify(content)

@autor_blueprint.route('/autor', methods=['DELETE'])
@jwt_required()
def delete_autor():
    data = request.get_json()
    if not data or 'autor_id' not in data:
        return jsonify({"error": "autor_id es requerido"}), 400
    return jsonify(autor_model.eliminar_autor(data['autor_id']))

@autor_blueprint.route('/autor', methods=['GET'])
@jwt_required()
def get_autor():
    data = request.get_json()
    if not data or 'autor_id' not in data:
        return jsonify({"error": "autor_id es requerido"}), 400
    return jsonify(autor_model.obtener_autor(data['autor_id']))

@autor_blueprint.route('/autores', methods=['GET'])
@jwt_required()
def get_autores():
    return jsonify(autor_model.obtener_autores())
