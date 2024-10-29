from app.repositories.psychologist_repository import PsychologistRepository
from app.repositories.user_repository import UserRepository
from app.models.psychologist import Psychologist
from app.models.user import User
from app.exceptions.conflict_exception import ConflictException

class PsychologistService:

    def get_psychologist_by_id(self, psychologist_id):
        return PsychologistRepository.get_psychologist_data(psychologist_id)

    def create_psychologist(self, name, email, password, crp, cpf, phone):
        if UserRepository.find_by_email(email):
            raise ConflictException("User with this email already exists")

        user = User(name=name, email=email)
        user.set_password(password)
        UserRepository.create_user(user)

        psychologist = Psychologist(crp=crp, cpf=cpf, phone=phone, user=user)
        return PsychologistRepository.create_psychologist(psychologist)

    def update_psychologist(self, data):
        try:
            return PsychologistRepository.update_psychologist_data(data)
        except Exception as e:
            print(f"Erro ao atualizar: {e}")
            return False