from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.services.psychologist_service import PsychologistService
from app.exceptions.conflict_exception import ConflictException

psychologist_bp = Blueprint('psychologist_routes', __name__, url_prefix='/psicologo')

psychologist_service = PsychologistService()

@psychologist_bp.route('/detalhe', methods=['GET'])
@jwt_required()
def get_psychologist_details():
    psychologist_id = get_jwt_identity()
    psychologist = psychologist_service.get_psychologist_by_id(psychologist_id)
    if psychologist:
        return jsonify({
            "name": psychologist.user.name,
            "email": psychologist.user.email,
            "cpf": psychologist.cpf,
        }), 200
    return jsonify({"error": "Psychologist not found"}), 404

@psychologist_bp.route('', methods=['POST'])
def create_psychologist():
    data = request.get_json()
    try:
        result = psychologist_service.create_psychologist(
            name=data['name'],
            email=data['email'],
            password=data['password'],
            crp=data['crp'],
            cpf=data['cpf'],
            phone=data['phone']
        )
        return jsonify({"message": "Psicólogo criado com sucesso!"}), 201
    except ConflictException as e:
        return jsonify({"error": str(e)}), 409

@psychologist_bp.route('/editar', methods=['PUT'])
@jwt_required()
def edit_psychologist():
    data = request.get_json()
    psychologist_id = get_jwt_identity()
    data['id'] = psychologist_id
    result = psychologist_service.update_psychologist(data)
    if result:
        return jsonify({"message": "Psychologist updated successfully"}), 200
    return jsonify({"error": "Failed to update psychologist"}), 400