from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from backend.models.mysql_genero_model import GeneroModel

genero_model = GeneroModel()
genero_blueprint = Blueprint('genero_blueprint', __name__)

@genero_blueprint.route('/genero', methods=['POST'])
@jwt_required()
def create_genero():
    data = request.get_json()
    if not data or 'nombre_genero' not in data:
        return jsonify({"error": "nombre_genero es requerido"}), 400
    return jsonify(genero_model.crear_genero(data['nombre_genero']))

@genero_blueprint.route('/genero', methods=['PUT'])
@jwt_required()
def update_genero():
    data = request.get_json()
    if not data or 'genero_id' not in data or 'nuevo_nombre' not in data:
        return jsonify({"error": "genero_id y nuevo_nombre son requeridos"}), 400
    return jsonify(genero_model.actualizar_genero(data['genero_id'], data['nuevo_nombre']))

@genero_blueprint.route('/genero', methods=['DELETE'])
@jwt_required()
def delete_genero():
    data = request.get_json()
    if not data or 'genero_id' not in data:
        return jsonify({"error": "genero_id es requerido"}), 400
    return jsonify(genero_model.eliminar_genero(data['genero_id']))

@genero_blueprint.route('/genero', methods=['GET'])
@jwt_required()
def get_genero():
    data = request.get_json()
    if not data or 'genero_id' not in data:
        return jsonify({"error": "genero_id es requerido"}), 400
    return jsonify(genero_model.obtener_genero(data['genero_id']))

@genero_blueprint.route('/generos', methods=['GET'])
@jwt_required()
def get_generos():
    return jsonify(genero_model.obtener_generos())
