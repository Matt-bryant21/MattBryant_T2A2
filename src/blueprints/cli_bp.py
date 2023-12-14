from flask import Blueprint
from setup import db, bcrypt
from models.models import Divisions, UFC_users, Fighters

db_commands = Blueprint('db', __name__)

# create all tables
@db_commands.cli.command("create")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()
    print("Tables created")

# seed all new tables with respective data
@db_commands.cli.command("seed")
def seed_db():
    # seed users
    admin_user = UFC_users(
        username="dana_white",
        password=bcrypt.generate_password_hash("1234").decode('utf-8'),
        role="admin"
    )
    user = UFC_users(
        username="referee",
        password=bcrypt.generate_password_hash("stoppage").decode('utf-8'),
        role="referee"
    )
    user2 = UFC_users(
        username="spectator",
        password=bcrypt.generate_password_hash("spectator1234").decode('utf-8'),
        role="spectator"
    )
    db.session.add(admin_user)
    db.session.add(user)
    db.session.add(user2)
    db.session.commit()
    print("Users seeded")

    # seed divisions
    flyweight = Divisions(name="Flyweight", description=f"Up to {126} lb ({round(126 * 0.453592, 2)} kg)")
    db.session.add(flyweight)

    bantamweight = Divisions(name="Bantamweight", description=f"Up to {135} lb ({round(135 * 0.453592, 2)} kg)")
    db.session.add(bantamweight)

    featherweight = Divisions(name="Featherweight", description=f"Up to {145} lb ({round(145 * 0.453592, 2)} kg)")
    db.session.add(featherweight)

    lightweight = Divisions(name="Lightweight", description=f"Up to {155} lb ({round(155 * 0.453592, 2)} kg)")
    db.session.add(lightweight)

    welterweight = Divisions(name="Welterweight", description=f"Up to {170} lb ({round(170 * 0.453592, 2)} kg)")
    db.session.add(welterweight)

    middleweight = Divisions(name="Middleweight", description=f"Up to {185} lb ({round(185 * 0.453592, 2)} kg)")
    db.session.add(middleweight)

    light_heavyweight = Divisions(name="Light_heavyweight",
                                  description=f"Up to {205} lb ({round(205 * 0.453592, 2)} kg)")
    db.session.add(light_heavyweight)

    heavyweight = Divisions(name="Heavyweight", description=f"Over {205} lb ({round(205 * 0.453592, 2)} kg)")
    db.session.add(heavyweight)

    db.session.commit()
    print("Divisions seeded")

    # seed fighters
    alex_volk = Fighters(
        name="Alexander Volkanovski",
        age=35,
        height=167.0,
        weight=145.0,
        division_id=lightweight.id,
        record="23/3/0",
        user_id=admin_user.id
    )
    db.session.add(alex_volk)

    jon_jones = Fighters(
        name="Jon Bones Jones",
        age=36,
        height=195.0,
        weight=248.0,
        division_id=heavyweight.id,
        record="27/1/0",
        user_id=admin_user.id
    )
    db.session.add(jon_jones)

    matt_bryant = Fighters(
        name="Matt Bryant",
        age=29,
        height=170.0,
        weight=145.0,
        division_id=lightweight.id,
        record="300/0/0",
        user_id=admin_user.id
    )
    db.session.add(matt_bryant)

    tom_aspinall = Fighters(
            name="Tom Aspinall",
            age=30,
            height=198.0,
            weight=216.0,
            division_id=heavyweight.id,
            record="14/3/0",
            user_id=admin_user.id
    )
    db.session.add(tom_aspinall)

    nate_diaz = Fighters(
        name="Nate Diaz",
        age=38,
        height=183.0,
        weight=169.0,
        division_id=lightweight.id,
        record="22/13/0",
        user_id=admin_user.id
    )
    db.session.add(nate_diaz)
    
    robbie_lawler = Fighters(
        name="Robbie Lawler",
        age=41,
        height=180.0,
        weight=169.0,
        division_id=welterweight.id,
        record="30/16/0",
        user_id=admin_user.id
    )
    db.session.add(robbie_lawler)
    
    conor_mcgregor = Fighters(
        name="Conor Mcgregor",
        age=35,
        height=175.0,
        weight=154.0,
        division_id=lightweight.id,
        record="22/6/0",
        user_id=admin_user.id
    )
    db.session.add(conor_mcgregor)
    
    justin_gaethje = Fighters(
        name="Justin Gaethje",
        age=35,
        height=180.0,
        weight=154.0,
        division_id=lightweight.id,
        record="25/4/0",
        user_id=admin_user.id
    )
    db.session.add(justin_gaethje)


    db.session.commit()
    print("Fighters seeded")