from app.models.patient_report import PatientReport
from sqlalchemy.orm import Session
from app.config.database import db

class PatientReportRepository:

    @staticmethod
    def create_report(report: PatientReport):
        db.session.add(report)
        db.session.commit()
        db.session.refresh(report)
        return report

    @staticmethod
    def delete_report(report_id: int):
        report = db.session.query(PatientReport).filter_by(id=report_id).first()
        if report:
            db.session.delete(report)
            db.session.commit()

    @staticmethod
    def get_reports_by_patient(patient_id: int):
        return db.session.query(PatientReport).filter_by(patient_id=patient_id).all()
