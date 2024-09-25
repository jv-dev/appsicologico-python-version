from app.repositories.user_repository import UserRepository
from app.exceptions.invalid_credentials_exception import InvalidCredentialsException
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash

class AuthService:

    def login(self, email, password):
        user = UserRepository.find_by_email(email)
        
        if not user or not check_password_hash(user.password_hash, password):
            raise InvalidCredentialsException("Invalid email or password")

        # Gerar token JWT
        access_token = create_access_token(identity=user.email)
        return {"access_token": access_token}
