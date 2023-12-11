from setup import app
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp
from blueprints.fighters_bp import fighters_bp
from blueprints.cli_bp import db_commands
from blueprints.divisions_bp import divisions_bp
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import json

app.register_blueprint(db_commands)
app.register_blueprint(users_bp)
app.register_blueprint(fighters_bp)
app.register_blueprint(divisions_bp)


if __name__ == '__main__':
    app.run(debug=True)
