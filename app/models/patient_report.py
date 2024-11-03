from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.config.database import db

class PatientReport(db.Model):
    __tablename__ = 'patient_reports'
    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    report_content = Column(String, nullable=False)
    report_date = Column(Date, nullable=False)
