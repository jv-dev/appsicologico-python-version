from app.repositories.psychologist_repository import PsychologistRepository
from app.repositories.user_repository import UserRepository
from app.models.psychologist import Psychologist
from app.models.user import User
from app.exceptions.conflict_exception import ConflictException

class PsychologistService:

    def create_psychologist(self, name, email, password, crp, cpf, phone):
        # Verificar se o usuário já existe
        if UserRepository.find_by_email(email):
            raise ConflictException("User with this email already exists")

        # Criar o usuário
        user = User(name=name, email=email)
        user.set_password(password)
        UserRepository.create_user(user)

        # Criar o psicólogo associado
        psychologist = Psychologist(crp=crp, cpf=cpf, phone=phone, user=user)
        return PsychologistRepository.create_psychologist(psychologist)
