from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from app.config.database import db

Base = declarative_base()

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_username(self):
        return self.email

    def is_account_non_expired(self):
        return True

    def is_account_non_locked(self):
        return True

    def is_credentials_non_expired(self):
        return True

    def is_enabled(self):
        return True
