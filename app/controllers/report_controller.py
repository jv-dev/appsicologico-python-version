from flask import Blueprint, jsonify, request, send_file
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.services.report_service import ReportService

report_bp = Blueprint('report_bp', __name__, url_prefix='/relatorio')

@report_bp.route('/atestado', methods=['POST'])
@jwt_required()
def create_medical_leave():
    data = request.get_json()
    psychologist_id = get_jwt_identity()
    data['psychologist_id'] = psychologist_id

    try:
        pdf = ReportService.create_medical_leave(data)
        return send_file(pdf, as_attachment=True, download_name='atestado.pdf', mimetype='application/pdf')
    except Exception as e:
        return jsonify({"msg": str(e)}), 400