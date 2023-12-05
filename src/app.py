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

@app.cli.command("create")
def create_db():
    db.create_all()
    print("Tables created")
    
@app.cli.command("seed")
def seed_db():
    # create the first card object
    alex_volk = Fighter(
        # set the attributes, not the id, SQLAlchemy will manage that for us
        name = "Alexander Volkanovski",
        age = "35",
        height = "167",
        weight = "145",
        division = "Lightweight",
        record = "23/3/0"
    )
    # Add the object as a new row to the table
    db.session.add(alex_volk)
    db.session.commit()
    print("Table seeded")

@app.route('/')
def hello():
    return 'Hello'