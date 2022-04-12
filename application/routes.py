from application import app, db
from application.forms import EntryForm
from application.models import Games
from flask import render_template, request, redirect, url_for


@app.route('/add_game', methods=['GET', 'POST'])
def add_game():
    form = EntryForm()
    if request.method == "POST":
        game = Games(game_date=form.game_date.data,
        team_name=form.team_name.data,
        home_away=form.home_away.data,
        result=form.result.data,
        opponent=form.result.data,
        comment=form.comment.data)
        db.session.add(game)
        db.session.commit()
        return redirect(url_for('all_entries'))

    return render_template('add_game.html', form=form)

@app.route('/all_entries')
def all_entries():
    all_games = Games.query.all()
    return render_template('all_entries.html', all_games=all_games)

