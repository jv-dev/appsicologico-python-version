from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.config.config import Config
from app.controllers.patient_controller import patient_bp
from app.controllers.psychologist_controller import psychologist_bp
from app.controllers.authenticate_controller import auth_bp
from app.controllers.report_controller import report_bp
from app.config.database import db

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(Config)
    
    db.init_app(app)
    JWTManager(app)

    app.register_blueprint(report_bp)
    app.register_blueprint(psychologist_bp)
    app.register_blueprint(patient_bp)
    app.register_blueprint(auth_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)