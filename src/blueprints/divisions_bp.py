from flask import Blueprint, request, jsonify
from models.models import Divisions
from setup import bcrypt, db
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import json

divisions_bp = Blueprint("divisions", __name__, url_prefix="/divisions")

ALLOWED_ROLES = ['admin', 'referee', 'spectator']