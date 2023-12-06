from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import json
from os import environ

app = Flask(__name__)

ALLOWED_ROLES = ['admin', 'referee', 'spectator']

# set the database URI via SQLAlchemy, 
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = environ.get('SECRET_KEY')  # Change this to a strong secret key
app.config["JWT_SECRET_KEY"] = environ.get('JWT_SECRET_KEY')  # Change this to a strong JWT secret key

# create the database and auth objects
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Create divisions table
class Division(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<Division {self.name}>"

# Create fighters table
class Fighter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)

    division_id = db.Column(db.Integer, db.ForeignKey('division.id'), nullable=False)
    division = db.relationship('Division', backref=db.backref('fighters', lazy=True))

    record = db.Column(db.String(20))

    user_id = db.Column(db.Integer, db.ForeignKey('ufc_user.id'), nullable=False)
    user = db.relationship('UFC_user', backref=db.backref('fighters', lazy=True))

    def __repr__(self):
        return f"<Fighter {self.name}>"

# Create users table
class UFC_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)

# Create all tables
@app.cli.command("create")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("Tables created")

# Seed all new tables with respective data 
@app.cli.command("seed")
def seed_db():
    # Seed users
    admin_user = UFC_user(
        username="daniel_white",
        password=bcrypt.generate_password_hash("1234").decode('utf-8'),
        role="admin"
    )
    user = UFC_user(
        username="referee",
        password=bcrypt.generate_password_hash("stoppage").decode('utf-8'),
        role="referee"
    )
    user2 = UFC_user(
        username="spectator",
        password=bcrypt.generate_password_hash("spectator1234").decode('utf-8'),
        role="spectator"
    )
    db.session.add(admin_user)
    db.session.add(user)
    db.session.add(user2)
    db.session.commit()
    print("User seeded")

    # Seed divisions
    flyweight = Division(name="Flyweight", description=f"Up to {126} lb ({round(126 * 0.453592, 2)} kg)")
    db.session.add(flyweight)

    bantamweight = Division(name="Bantamweight", description=f"Up to {135} lb ({round(135 * 0.453592, 2)} kg)")
    db.session.add(bantamweight)

    featherweight = Division(name="Featherweight", description=f"Up to {145} lb ({round(145 * 0.453592, 2)} kg)")
    db.session.add(featherweight)

    lightweight = Division(name="Lightweight", description=f"Up to {155} lb ({round(155 * 0.453592, 2)} kg)")
    db.session.add(lightweight)

    welterweight = Division(name="Welterweight", description=f"Up to {170} lb ({round(170 * 0.453592, 2)} kg)")
    db.session.add(welterweight)

    middleweight = Division(name="Middleweight", description=f"Up to {185} lb ({round(185 * 0.453592, 2)} kg)")
    db.session.add(middleweight)

    light_heavyweight = Division(name="Light_heavyweight", description=f"Up to {205} lb ({round(205 * 0.453592, 2)} kg)")
    db.session.add(light_heavyweight)

    heavyweight = Division(name="Heavyweight", description=f"Over {205} lb ({round(205 * 0.453592, 2)} kg)")
    db.session.add(heavyweight)

    db.session.commit()
    print("Divisions seeded")

    # Seed fighters
    alex_volk = Fighter(
        name="Alexander Volkanovski",
        age=35,
        height=167.0,
        weight=145.0,
        division_id=lightweight.id,
        record="23/3/0",
        user_id=admin_user.id 
    )
    db.session.add(alex_volk)

    jon_jones = Fighter(
        name="Jon Bones Jones",
        age=36,
        height=195.0,
        weight=248.0,
        division_id=heavyweight.id,
        record="27/1/0",
        user_id=admin_user.id 
    )
    db.session.add(jon_jones)

    Matt_bryant = Fighter(
        name="Matt Bryant",
        age=29,
        height=170.0,
        weight=145.0,
        division_id=lightweight.id,
        record="300/0/0",
        user_id=admin_user.id 
    )
    db.session.add(Matt_bryant)

    db.session.commit()
    print("Fighters seeded")

# Endpoints 

# register user
@app.route('/register', methods=['POST'])
@jwt_required()
def register():
    # Check if the current user has the "admin" role
    current_user = get_jwt_identity()
    user = UFC_user.query.filter_by(username=current_user['username']).first()

    current_user = get_jwt_identity()
    if 'admin' not in current_user['role']:
        return jsonify({'message': 'Unauthorized'}), 403
    
    # Proceed with user registration
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')
    role = data.get('role')

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = UFC_user(username=username, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201

# User login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    user = UFC_user.query.filter_by(username=username).first()

    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity={'username': user.username, 'role': user.role})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

# delete fighter 
@app.route('/delete_fighter/<int:fighter_id>', methods=['DELETE'])
@jwt_required()
def delete_fighter(fighter_id):
    
    current_user = get_jwt_identity()
    if 'admin' not in current_user['role']:
        return jsonify({'message': 'Unauthorized'}), 403

    fighter = Fighter.query.get(fighter_id)

    if fighter:
        db.session.delete(fighter)
        db.session.commit()
        return jsonify({'message': 'Fighter deleted successfully'}), 200
    else:
        return jsonify({'message': 'Fighter not found'}), 404

# View fighter 
@app.route('/view_fighter/<int:fighter_id>', methods=['GET'])
@jwt_required()
def view_fighter(fighter_id):
    current_user = get_jwt_identity()

    # Check if the user's role is in the allowed roles
    if any(role in current_user['role'] for role in ALLOWED_ROLES):
        fighter = Fighter.query.get(fighter_id)
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

            # Use json.dumps for strict control over key order
            response_json = json.dumps(fighter_info, sort_keys=True, indent=2)
            return response_json, 200, {'Content-Type': 'application/json'}
        else:
            return jsonify({'message': 'Fighter not found'}), 404
    else:
        return jsonify({'message': 'Unauthorized'}), 403

if __name__ == '__main__':
    app.run(debug=True)
