from application import db
from datetime import datetime

class Teams(db.Model):
    team_name = db.Column(db.String(30), primary_key=True, nullable=False)
    manager = db.Column(db.String(30), nullable=False)
    ground = db.Column(db.String(30), nullable=False)

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fk_team_name = db.Column(db.String(30), db.ForeignKey('teams.team_name'), nullable=False)
    game_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    home_away = db.Column(db.String(4), nullable=False)
    result = db.Column(db.String(4), nullable=False)
    opponent = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(100), nullable=True)
    included = db.Column(db.Boolean, nullable=False, default=False)

