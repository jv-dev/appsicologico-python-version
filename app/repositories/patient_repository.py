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
            rg=data['rg'],
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
    def get_all(page=1, per_page=10):
        return Patient.query.paginate(page=page, per_page=per_page, error_out=False)

    def get_by_id(patient_id):
        try:
            patient_id = int(patient_id)
        except ValueError:
            raise ValueError("O ID do paciente deve ser um número inteiro válido.")

        patient = Patient.query.get(patient_id)
        
        if not patient:
            raise PatientNotFound(f"Paciente com ID {patient_id} não encontrado.")
        
        return patient
    
    def get_by_cpf(patient_cpf):
        patient = Patient.query.filter_by(cpf=patient_cpf).first()
        
        return patient
    
    def get_by_rg(patient_rg):
        patient = Patient.query.filter_by(rg=patient_rg).first()
        
        return patient