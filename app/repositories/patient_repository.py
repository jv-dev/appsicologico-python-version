from app.models.patient import Patient
from app.config.database import db
from app.exceptions.patient_exceptions import PatientNotFound

class PatientRepository:

    @staticmethod
    def create(data):
        patient = Patient(
            name=data['name'],
            cpf=data['cpf'],
            email=data['email'],
            birth_date=data['birth_date'],
            rg=data['rg']
        )
        db.session.add(patient)
        db.session.commit()

    @staticmethod
    def update(id, data):
        patient = Patient.query.get(id)
        if not patient:
            raise PatientNotFound()

        patient.name = data['name']
        patient.cpf = data['cpf']
        patient.email = data['email']
        patient.birth_date = data['birth_date']
        patient.rg = data['rg']

        db.session.commit()

    @staticmethod
    def delete(id):
        patient = Patient.query.get(id)
        if not patient:
            raise PatientNotFound()

        db.session.delete(patient)
        db.session.commit()

    @staticmethod
    def get_all():
        return Patient.query.all()

    @staticmethod
    def get_by_id(patient_id):
        patient = Patient.query.get(patient_id)
        if not patient:
            raise PatientNotFound()
        return patient
