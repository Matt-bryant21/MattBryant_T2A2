from flask import Blueprint, request, jsonify
from models.models import Divisions
from setup import bcrypt, db
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import json

divisions_bp = Blueprint("divisions", __name__, url_prefix="/divisions")

ALLOWED_ROLES = ['admin', 'referee', 'spectator']

# create division
@divisions_bp.route('/create_division', methods=['POST'])
@jwt_required()
def create_division():
    current_user = get_jwt_identity()

    # check if the user's role is admin
    if 'admin' not in current_user['role']:
        return jsonify({'message': 'Unauthorized'}), 403

    # cet data from the request body
    data = request.get_json()

    # assuming you have all the required fields in the data
    name = data.get('name')
    description = data.get('description')

    # check if all required fields are present
    if not all([name, description]):
        return jsonify({'message': 'Incomplete data'}), 400

    # check if the division with the same name already exists
    existing_division = Divisions.query.filter_by(name=name).first()
    if existing_division:
        return jsonify({'message': 'Division with the same name already exists'}), 400

    # create a new division
    new_division = Divisions(
        name=name,
        description=description
    )

    # add the division to the database
    db.session.add(new_division)
    db.session.commit()

    return jsonify({'message': 'Division created successfully'}), 201


# view division
@divisions_bp.route('/view_division/<int:division_id>', methods=['GET'])
@jwt_required()
def view_division(division_id):
    current_user = get_jwt_identity()

    # check if the user's role is in the allowed roles
    if any(role in current_user['role'] for role in ALLOWED_ROLES):
        division = Divisions.query.get(division_id)
        if division:
            # create a dictionary with the division information
            division_info = {
                'id': division.id,
                'name': division.name,
                'description': division.description
            }

            # use json.dumps for control over key order
            response_json = json.dumps(division_info, sort_keys=True, indent=2)
            return response_json, 200, {'Content-Type': 'application/json'}
        else:
            return jsonify({'message': 'Division not found'}), 404
    else:
        return jsonify({'message': 'Unauthorized'}), 403


# update division
@divisions_bp.route('/update_division/<int:division_id>', methods=['PUT'])
@jwt_required()
def update_division(division_id):
    current_user = get_jwt_identity()

    # check if the user's role is admin
    if 'admin' not in current_user['role'] and 'referee' not in current_user['role']:
        return jsonify({'message': 'Unauthorized'}), 403

    # get data from the request body
    try:
        data = request.get_json()
    except:
        return jsonify({'message': 'Invalid JSON format in the request body'}), 400

    # check if all required fields are present
    if not isinstance(data, dict) or 'name' not in data or 'description' not in data:
        return jsonify({'message': 'Incomplete or invalid data in the request body'}), 400

    # check if the division exists
    division = Divisions.query.get(division_id)
    if not division:
        return jsonify({'message': 'Division not found'}), 404

    # update the division data
    division.name = data['name']
    division.description = data['description']

    # commit the changes to the database
    db.session.commit()

    return jsonify({'message': 'Division updated successfully'}), 200


# delete division
@divisions_bp.route('/delete_division/<int:division_id>', methods=['DELETE'])
@jwt_required()
def delete_division(division_id):
    current_user = get_jwt_identity()
    if 'admin' not in current_user['role']:
        return jsonify({'message': 'Unauthorized'}), 403

    division = Divisions.query.get(division_id)

    if division:
        db.session.delete(division)
        db.session.commit()
        return jsonify({'message': 'Division deleted successfully'}), 200
    else:
        return jsonify({'message': 'Division not found'}), 404