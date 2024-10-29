from flask import render_template
from app.repositories.patient_repository import PatientRepository
from app.exceptions.patient_exceptions import PatientNotFound
from datetime import datetime
from xhtml2pdf import pisa
from app.repositories.psychologist_repository import PsychologistRepository
from io import BytesIO

class ReportService:

    @staticmethod
    def format_cpf(cpf_str):
        return f"{cpf_str[:3]}.{cpf_str[3:6]}.{cpf_str[6:9]}-{cpf_str[9:]}"

    @staticmethod
    def create_medical_leave(data):
        patient_id = data.get('patient_id')
        psychologist_id = data.get('psychologist_id')

        patient = PatientRepository.get_by_id(patient_id)
        psychologist = PsychologistRepository.get_by_id(psychologist_id)

        psychologist_data = f'{psychologist.user.name}. CRP: {psychologist.crp}'
        patient_data = patient.name
        cpf = ''.join(filter(str.isdigit, patient.cpf))
        formatted_cpf = ReportService.format_cpf(cpf)

        data_dict = {
            'date': datetime.now().strftime('%d/%m/%Y'),
            'psychologist_data': psychologist_data,
            'psychologist_email': psychologist.user.email,
            'patient_data': patient_data,
            'patient_document': formatted_cpf
        }

        html = render_template('medical_leave.html', **data_dict)
        pdf = BytesIO()
        pisa.CreatePDF(html, dest=pdf)

        pdf.seek(0)
        return pdf