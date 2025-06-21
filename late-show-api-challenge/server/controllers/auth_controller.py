from flask import Blueprint, request, jsonify
from server.models.user import User
from server.app import db
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods='POST')
def register():
    data = register.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400
    
    if user.query.filter_by(username=username).first():
        return jsonify({"error": "username already exists"}), 409
    
    user = user(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "user created successfully"}), 201


