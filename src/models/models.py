from setup import db

# create divisions table
class Divisions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return f"<Division {self.name}>"


# create users table
class UFC_users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(20), nullable=False)


# create fighters table
class Fighters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)

    division_id = db.Column(db.Integer, db.ForeignKey('divisions.id'), nullable=False)
    division = db.relationship('Divisions', backref=db.backref('fighters', lazy=True))

    record = db.Column(db.String(20))

    user_id = db.Column(db.Integer, db.ForeignKey('ufc_users.id'), nullable=False)
    user = db.relationship('UFC_users', backref=db.backref('fighters', lazy=True))

    def __repr__(self):
        return f"<Fighter {self.name}>"


