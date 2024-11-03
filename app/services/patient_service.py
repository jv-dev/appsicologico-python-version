import os
from flask_jwt_extended import get_jwt_identity
from app.repositories.patient_psychologist_repository import PatientPsychologistRepository
from app.repositories.patient_repository import PatientRepository
from app.exceptions.patient_exceptions import PatientNotFound
from datetime import datetime

class PatientService:

    def create_patient(data):
        if not all([data.get('name'), data.get('cpf'), data.get('email'), data.get('birth_date'), data.get('rg')]):
            raise ValueError("All fields are required")

        data['birth_date'] = datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
        data['cpf'] = data['cpf'].replace('.', '').replace('-', '')
        data['rg'] = data['rg'].replace('.', '').replace('-', '')

        existing_patient_cpf = PatientRepository.get_by_cpf(data['cpf'])
        existing_patient_rg = PatientRepository.get_by_rg(data['rg'])

        existing_patient = True if existing_patient_cpf or existing_patient_rg else False
        patient_id = None
        if existing_patient_cpf:
           patient_id = existing_patient_cpf.id
        elif existing_patient_rg:
           patient_id = existing_patient_rg.id
        
        psychologist_id = get_jwt_identity()

        if existing_patient:
            PatientPsychologistRepository.create_relationship(patient_id, psychologist_id)
        else:
            new_patient = PatientRepository.create(data)
            PatientPsychologistRepository.create_relationship(new_patient.id, psychologist_id)

    @staticmethod
    def update_patient(id, data):
        if not all([data.get('name'), data.get('cpf'), data.get('email'), data.get('birth_date'), data.get('rg')]):
            raise ValueError("All fields are required")

        data['birth_date'] = datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
        data['cpf'] = data['cpf'].replace('.', '').replace('-', '')
        data['rg'] = data['rg'].replace('.', '').replace('-', '')

        existing_patient_cpf = PatientRepository.get_by_cpf(data['cpf'])
        if existing_patient_cpf and existing_patient_cpf.id != id:
            raise Exception('CPF já cadastrado')
        
        existing_patient_rg = PatientRepository.get_by_rg(data['rg'])
        if existing_patient_rg and existing_patient_rg.id != id:
            raise Exception('RG já cadastrado')

        PatientRepository.update(id, data)

    @staticmethod
    def delete_patient(id):
        PatientRepository.delete(id)

    @staticmethod
    def get_all_patients(page=1, per_page=10):
        paginated_data = PatientRepository.get_all(page, per_page)
        return {
            "patients": [{
                "id": patient.id,
                "name": patient.name,
                "cpf": patient.cpf,
                "email": patient.email,
                "birth_date": patient.birth_date.strftime('%Y-%m-%d'),
                "rg": patient.rg
            } for patient in paginated_data.items],
            "total": paginated_data.total,
            "pages": paginated_data.pages,
            "current_page": paginated_data.page
        }

    @staticmethod
    def get_patient_by_id(patient_id):
        return PatientRepository.get_by_id(patient_id)
