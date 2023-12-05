from flask import Flask
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)

# set the database URI via SQLAlchemy, 
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://dana_white:1234@localhost:5432/ufc"

#create the database object
db = SQLAlchemy(app)

class Division(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<Division {self.name}>"


class Fighter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    
    division_id = db.Column(db.Integer, db.ForeignKey('division.id'), nullable=False)
    division = db.relationship('Division', backref=db.backref('fighters', lazy=True))
    
    record = db.Column(db.String(20))

    def __repr__(self):
        return f"<Fighter {self.name}>"

@app.cli.command("create")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("Tables created")


@app.cli.command("seed")
def seed_db():
    # Seed divisions
    lightweight = Division(name="Lightweight", description="Up to 155 lb (70.31 kg)")
    db.session.add(lightweight)

    heavyweight = Division(name="Heavyweight", description="Over 205 lb (93 kg)")
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
        record="23/3/0"
    )
    db.session.add(alex_volk)

    jon_jones = Fighter(
        name="Jon Bones Jones",
        age=36,
        height=195.0,
        weight=248.0,
        division_id=heavyweight.id,
        record="27/1/0"
    )
    db.session.add(jon_jones)

    db.session.commit()
    print("Fighters seeded")


@app.route('/')
def hello():
    return 'Hello'