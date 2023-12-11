from flask import Blueprint, request, jsonify
from models.models import Fighters, Divisions, UFC_users
from setup import bcrypt, db
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import json

fighters_bp = Blueprint("fighters", __name__, url_prefix="/fighters")

ALLOWED_ROLES = ['admin', 'referee', 'spectator']

# Create new fighter
@fighters_bp.route('/add_fighter', methods=['POST'])
@jwt_required()
def add_fighter():
    current_user = get_jwt_identity()

    # Check if the user's role is admin
    if 'admin' not in current_user['role']:
        return jsonify({'message': 'Unauthorized'}), 403

    # Get data from the request body
    data = request.get_json()

    # Assuming you have all the required fields in the data
    name = data.get('name')
    age = data.get('age')
    height = data.get('height')
    weight = data.get('weight')
    record = data.get('record')
    division_id = data.get('division_id')  # Assuming you have a division_id in the data

    # Check if all required fields are present
    if not all([name, age, height, weight, record, division_id]):
        return jsonify({'message': 'Incomplete data'}), 400

    # Check if the division exists
    division = Divisions.query.get(division_id)
    if not division:
        return jsonify({'message': 'Division not found'}), 404


    user = UFC_users.query.filter_by(username=current_user['username']).first()

    if not user:
        return jsonify({'message': 'User not found'}), 404


    # Create a new fighter with the current user's ID
    new_fighter = Fighters(
        name=name,
        age=age,
        height=height,
        weight=weight,
        record=record,
        division=division,
        user_id=user.id
    )

    # Add the fighter to the database
    db.session.add(new_fighter)
    db.session.commit()

    return jsonify({'message': 'Fighter added successfully'}), 201


# View fighter
@fighters_bp.route('/view_fighter/<int:fighter_id>', methods=['GET'])
@jwt_required()
def view_fighter(fighter_id):
    current_user = get_jwt_identity()

    # Check if the user's role is in the allowed roles
    if any(role in current_user['role'] for role in ALLOWED_ROLES):
        fighter = Fighters.query.get(fighter_id)
        if fighter:
            # Create a dictionary with the desired order
            fighter_info = {
                'id': fighter.id,
                'name': fighter.name,
                'age': fighter.age,
                'height': fighter.height,
                'weight': fighter.weight,
                'division': {
                    'id': fighter.division.id,
                    'name': fighter.division.name,
                    'description': fighter.division.description
                },
                'record': fighter.record
            }

            # Use json.dumps for control over key order
            response_json = json.dumps(fighter_info, sort_keys=True, indent=2)
            return response_json, 200, {'Content-Type': 'application/json'}
        else:
            return jsonify({'message': 'Fighter not found'}), 404
    else:
        return jsonify({'message': 'Unauthorized'}), 403


# Update fighter information
@fighters_bp.route('/update_fighter/<int:fighter_id>', methods=['PUT'])
@jwt_required()
def update_fighter(fighter_id):
    current_user = get_jwt_identity()
    if 'admin' not in current_user['role'] and 'referee' not in current_user['role']:
        return jsonify({'message': 'Unauthorized'}), 403

    fighter = Fighters.query.get(fighter_id)

    if fighter:
        data = request.get_json()
        fighter.name = data.get('name', fighter.name)
        fighter.age = data.get('age', fighter.age)
        fighter.height = data.get('height', fighter.height)
        fighter.weight = data.get('weight', fighter.weight)
        fighter.record = data.get('record', fighter.record)

        # Assuming you also have a division_id in the data for updating the division
        division_id = data.get('division_id')
        if division_id:
            division = Divisions.query.get(division_id)
            if division:
                fighter.division = division
            else:
                return jsonify({'message': 'Division not found'}), 404

        db.session.commit()
        return jsonify({'message': 'Fighter updated successfully'}), 200
    else:
        return jsonify({'message': 'Fighter not found'}), 404
    

# delete fighter
@fighters_bp.route('/delete_fighter/<int:fighter_id>', methods=['DELETE'])
@jwt_required()
def delete_fighter(fighter_id):
    current_user = get_jwt_identity()
    if 'admin' not in current_user['role']:
        return jsonify({'message': 'Unauthorized'}), 403

    fighter = Fighters.query.get(fighter_id)

    if fighter:
        db.session.delete(fighter)
        db.session.commit()
        return jsonify({'message': 'Fighter deleted successfully'}), 200
    else:
        return jsonify({'message': 'Fighter not found'}), 404
