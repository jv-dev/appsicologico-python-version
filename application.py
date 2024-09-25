import os
from flask import Flask
from flask.cli import load_dotenv
from flask_jwt_extended import JWTManager
from app.config.database import db, init_db

app = Flask(__name__)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

# Inicializar o banco de dados com o app
db.init_app(app)

# Inicializar JWT
jwt = JWTManager(app)

# Criar as tabelas no banco de dados
with app.app_context():
    init_db(app)  # Cria as tabelas no banco de dados

from app.controllers import authenticate_controller
from app.controllers import psychologist_controller
app.register_blueprint(authenticate_controller.bp)
app.register_blueprint(psychologist_controller.bp)

if __name__ == '__main__':
    app.run(debug=True)
