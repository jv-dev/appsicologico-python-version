from app.models.psychologist import Psychologist
from app.config.database import db

class PsychologistRepository:

    @staticmethod
    def create_psychologist(psychologist):
        db.session.add(psychologist)
        db.session.commit()
        return psychologist

    @staticmethod
    def find_by_crp(crp):
        return Psychologist.query.filter_by(crp=crp).first()
