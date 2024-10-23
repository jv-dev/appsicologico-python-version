from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services.patient_service import PatientService

patient_bp = Blueprint('patient_bp', __name__, url_prefix='/paciente')

@patient_bp.route('/criar', methods=['POST'])
@jwt_required()
def create_patient():
    data = request.get_json()
    try:
        PatientService.create_patient(data)
        return jsonify({"msg": "Patient created successfully!"}), 201
    except Exception as e:
        return jsonify({"msg": str(e)}), 400

@patient_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_patient(id):
    data = request.get_json()
    try:
        PatientService.update_patient(id, data)
        return jsonify({"msg": "Patient updated successfully!"}), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 400

@patient_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_patient(id):
    try:
        PatientService.delete_patient(id)
        return jsonify({"msg": "Patient deleted successfully!"}), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 400

@patient_bp.route('/listar', methods=['GET'])
@jwt_required()
def get_all_patients():
    try:
        patients = PatientService.get_all_patients()
        return jsonify([{
            "id": patient.id,
            "name": patient.name,
            "cpf": patient.cpf,
            "email": patient.email,
            "birth_date": patient.birth_date.strftime('%Y-%m-%d'),
            "rg": patient.rg
        } for patient in patients]), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 400

@patient_bp.route('/buscar/<int:id>', methods=['GET'])
@jwt_required()
def get_patient_by_id(id):
    try:
        patient = PatientService.get_patient_by_id(id)
        return jsonify({
            "id": patient.id,
            "name": patient.name,
            "cpf": patient.cpf,
            "email": patient.email,
            "birth_date": patient.birth_date.strftime('%Y-%m-%d'),
            "rg": patient.rg
        }), 200
    except Exception as e:
        return jsonify({"msg": str(e)}), 400