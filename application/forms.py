from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired, Length

class EntryForm(FlaskForm):
    game_date = DateField("Date of game")
    team_name = SelectField('Choose Team', choices=[
        ("arsenal", "Arsenal"),
        ("chelsea", "Chelsea"),
        ("liverpool", "Liverpool"),
        ("man_city", "Manchester City"),
        ("man_utd", "Manchester United"),
        ("tottenham", "Tottenham")
    ])
    home_away = SelectField('Home or Away', choices=[
        ("home", "Home"),
        ("away", "Away")  
    ])
    result = SelectField('What was the result?', choices=[
        ("win", "Win"),
        ("loss", "Loss"),
        ("draw", "Draw")
    ])
    opponent = StringField('Which team did they play?', validators=[
        DataRequired(), 
        Length(max=30)
    ])
    comment = StringField('Any notes on the game', validators=[
        Length(max=100)
    ])
    submit = SubmitField('Add entry')
    




