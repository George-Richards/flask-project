from application import db
from datetime import datetime

class Games(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_date = db.Column(db.DateTime, nullable=False, default=datetime.now())
    team_name = db.Column(db.String(30), nullable=False)
    home_away = db.Column(db.String(4), nullable=False)
    result = db.Column(db.String(4), nullable=False)
    opponent = db.Column(db.String(100), nullable=False)
    comment = db.Column(db.String(100), nullable=True)

