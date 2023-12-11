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


# user login
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


# view user
@users_bp.route('/view_user/<int:user_id>', methods=['GET'])
@jwt_required()
def view_user(user_id):
    current_user = get_jwt_identity()

    # Check if the current user has the "admin" role
    if 'admin' not in current_user['role']:
        return jsonify({'message': 'Unauthorized'}), 403

    # Check if the user to be viewed exists
    user = UFC_users.query.get(user_id)

    if user:
        user_info = {
            'id': user.id,
            'username': user.username,
            'role': user.role
            # Add more fields as needed
        }

        return jsonify(user_info), 200
    else:
        return jsonify({'message': 'User not found'}), 404


@users_bp.route('/update_user/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    current_user = get_jwt_identity()

    # check if the user to be updated is the same as the authenticated user
    if user_id == current_user.get('id'):
        return jsonify({'message': 'Cannot update the current user'}), 400
  
    # check if the user to be updated exists
    user = UFC_users.query.get(user_id)

    if user:
        data = request.get_json()

        # verify the current password before proceeding
        current_password = data.get('current_password')
        if not bcrypt.check_password_hash(user.password, current_password):
            return jsonify({'message': 'Invalid current password'}), 400

        # update user information based on the data provided in the request
        user.username = data.get('username', user.username)
        user.role = data.get('role', user.role)

        # update password if provided
        new_password = data.get('new_password')
        if new_password:
            user.password = bcrypt.generate_password_hash(new_password).decode('utf-8')

        db.session.commit()
        return jsonify({'message': 'User updated successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404

# delete user
@users_bp.route('/delete_user/<int:user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    current_user = get_jwt_identity()

    # check if the current user has the "admin" role
    if 'admin' not in current_user['role']:
        return jsonify({'message': 'Unauthorized'}), 403

    # check if the user to be deleted is the same as the current user
    if user_id == current_user.get('id'):
        return jsonify({'message': 'Cannot delete the current user'}), 400

    # check if the user to be deleted exists
    user = UFC_users.query.get(user_id)

    if user:
        # check if there is more than one admin user
        admin_users_count = UFC_users.query.filter_by(role='admin').count()

        if admin_users_count <= 1 and user.role == 'admin':
            return jsonify({'message': 'Cannot delete the last admin user. Create another admin user first.'}), 400

        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404