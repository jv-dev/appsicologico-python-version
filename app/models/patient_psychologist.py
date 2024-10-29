from app.config.database import db

class PatientPsychologist(db.Model):
    __tablename__ = 'patient_psychologist'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id', ondelete='CASCADE'), nullable=False)
    psychologist_id = db.Column(db.Integer, db.ForeignKey('psychologists.id', ondelete='CASCADE'), nullable=False)