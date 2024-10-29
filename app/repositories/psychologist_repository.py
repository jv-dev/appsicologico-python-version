from app.models.psychologist import Psychologist
from app.config.database import db

class PsychologistRepository:

    @staticmethod
    def get_psychologist_data(psychologist_id):
        return Psychologist.query.filter_by(id=psychologist_id).first()

    @staticmethod
    def create_psychologist(psychologist):
        db.session.add(psychologist)
        db.session.commit()
        return psychologist
    
    @staticmethod
    def update_psychologist_data(data):
        psychologist = Psychologist.query.filter_by(id=data['id']).first()
        if not psychologist:
            return False
        psychologist.user.name = data['name']
        psychologist.cpf = data['cpf']
        db.session.commit()
        return True

    @staticmethod
    def find_by_crp(crp):
        return Psychologist.query.filter_by(crp=crp).first()
    
    @staticmethod
    def get_by_user_id(user_id):
        try:
            user_id = int(user_id)
        except ValueError:
            raise ValueError("O ID do psicólogo deve ser um número inteiro válido.")

        psychologist = Psychologist.query.filter_by(user_id=user_id).first()
        
        if not psychologist:
            raise Exception(f"Psicólogo com ID {user_id} não encontrado.")
        
        return psychologist

    @staticmethod
    def get_by_id(psychologist_id):
        try:
            psychologist_id = int(psychologist_id)
        except ValueError:
            raise ValueError("O ID do psicólogo deve ser um número inteiro válido.")

        psychologist = Psychologist.query.get(psychologist_id)
        
        if not psychologist:
            raise Exception(f"Psicólogo com ID {psychologist_id} não encontrado.")
        
        return psychologist