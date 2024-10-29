from app.config.database import db
from app.models.patient_psychologist import PatientPsychologist

class PatientPsychologistRepository:

    @staticmethod
    def create_relationship(patient_id, psychologist_id):
        existing_relationship = PatientPsychologist.query.filter_by(
            patient_id=patient_id, psychologist_id=psychologist_id
        ).first()

        if existing_relationship:
            raise Exception('Paciente já cadastrado')

        new_relationship = PatientPsychologist(patient_id=patient_id, psychologist_id=psychologist_id)
        db.session.add(new_relationship)
        db.session.commit()
        return "Relationship created successfully."
