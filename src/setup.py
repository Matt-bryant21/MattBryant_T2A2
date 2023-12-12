from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import json
from os import environ

app = Flask(__name__)

# set the database URI via SQLAlchemy,
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = environ.get('SECRET_KEY')  # Change this to a strong secret key
app.config["JWT_SECRET_KEY"] = environ.get('JWT_SECRET_KEY')  # Change this to a strong JWT secret key

# create the database and auth objects
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


# error handlers
@app.errorhandler(400)
def handle_bad_request(error):
    response = {'message': 'Bad request'}
    return jsonify(response), 400


def handle_exception(error):
    response = {'message': 'An unexpected error occurred'}
    return jsonify(response), 500


@app.errorhandler(404)
def handle_not_found(error):
    response = {'message': 'Resource not found'}
    return jsonify(response), 404


@app.errorhandler(401)
def handle_unauthorized(error):
    response = {'message': 'Unauthorized'}
    return jsonify(response), 401