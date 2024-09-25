from flask import Blueprint, request, jsonify
from app.services.psychologist_service import PsychologistService
from app.exceptions.conflict_exception import ConflictException

bp = Blueprint('psychologist_routes', __name__, url_prefix='/psicologo')

psychologist_service = PsychologistService()

@bp.route('/', methods=['POST'])
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
