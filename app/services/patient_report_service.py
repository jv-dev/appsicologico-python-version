from app.repositories.patient_report_repository import PatientReportRepository
from app.models.patient_report import PatientReport

class PatientReportService:

    @staticmethod
    def create_report(patient_id: int, report_content: str, report_date):
        new_report = PatientReport(patient_id=patient_id, report_content=report_content, report_date=report_date)
        return PatientReportRepository.create_report(new_report)

    @staticmethod
    def delete_report(report_id: int):
        PatientReportRepository.delete_report(report_id)

    @staticmethod
    def list_reports(patient_id: int):
        return PatientReportRepository.get_reports_by_patient(patient_id)
