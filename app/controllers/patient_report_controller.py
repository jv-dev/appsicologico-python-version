from flask import Blueprint, request, jsonify
from app.repositories.patient_report_repository import PatientReportRepository
from app.services.patient_report_service import PatientReportService

patient_report_bp = Blueprint('patient_report', __name__)

@patient_report_bp.route('/reports', methods=['POST'])
def create_report():
    data = request.json
    patient_id = data['patient_id']
    report_content = data['report_content']
    report_date = data['report_date']
    report = PatientReportService.create_report(patient_id, report_content, report_date)
    return jsonify({'id': report.id, 'message': 'Report created successfully'}), 201

@patient_report_bp.route('/reports/<int:report_id>', methods=['DELETE'])
def delete_report(report_id):
    PatientReportService.delete_report(report_id)
    return jsonify({'message': 'Report deleted successfully'}), 200

@patient_report_bp.route('/reports/patient/<int:patient_id>', methods=['GET'])
def get_reports(patient_id):
    reports = PatientReportService.list_reports(patient_id)
    return jsonify([{'id': r.id, 'content': r.report_content, 'date': r.report_date} for r in reports]), 200
  