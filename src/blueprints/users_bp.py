from flask import Blueprint, request, jsonify
from models.models import UFC_users
from setup import bcrypt, db
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import json

users_bp = Blueprint("users", __name__, url_prefix="/users")


ALLOWED_ROLES = ['admin', 'referee', 'spectator']

# register user
@users_bp.route('/register', methods=['POST'])
@jwt_required()
def register():
    # Check if the current user has the "admin" role
    current_user = get_jwt_identity()
    if 'admin' not in current_user['role']:
        return jsonify({'message': 'Unauthorized'}), 403

    # Proceed with user registration
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = UFC_users(username=username, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201


# User login
@users_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    user = UFC_users.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity={'username': user.username, 'role': user.role})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

