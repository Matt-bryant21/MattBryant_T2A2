from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)

# set the database URI via SQLAlchemy, 
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://dana_white:1234@localhost:5432/ufc"

#create the database object
db = SQLAlchemy(app)

class Fighter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    division = db.Column(db.String(50))
    record = db.Column(db.String(20))



@app.route('/')
def hello():
    return 'Hello'