from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService
from app.exceptions.invalid_credentials_exception import InvalidCredentialsException

auth_bp = Blueprint('auth_routes', __name__, url_prefix='/auth')

auth_service = AuthService()

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    try:
        token = auth_service.login(email=data['email'], password=data['password'])
        return jsonify(token), 200
    except InvalidCredentialsException as e:
        return jsonify({"error": str(e)}), 401
