from app.repositories.patient_repository import PatientRepository
from app.exceptions.patient_exceptions import PatientNotFound
from datetime import datetime

class PatientService:

    @staticmethod
    def create_patient(data):
        if not all([data.get('name'), data.get('cpf'), data.get('email'), data.get('birth_date'), data.get('rg')]):
            raise ValueError("All fields are required")

        data['birth_date'] = datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
        PatientRepository.create(data)

    @staticmethod
    def update_patient(id, data):
        if not all([data.get('name'), data.get('cpf'), data.get('email'), data.get('birth_date'), data.get('rg')]):
            raise ValueError("All fields are required")

        data['birth_date'] = datetime.strptime(data['birth_date'], '%Y-%m-%d').date()
        PatientRepository.update(id, data)

    @staticmethod
    def delete_patient(id):
        PatientRepository.delete(id)

    @staticmethod
    def get_all_patients():
        return PatientRepository.get_all()

    @staticmethod
    def get_patient_by_id(patient_id):
        return PatientRepository.get_by_id(patient_id)
