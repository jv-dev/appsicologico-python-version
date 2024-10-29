from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from app.config.database import db

Base = declarative_base()

class Psychologist(db.Model):
    __tablename__ = 'psychologists'

    id = Column(Integer, primary_key=True, autoincrement=True)
    crp = Column(String, unique=True, nullable=False)
    cpf = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")

