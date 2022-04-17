from application import app, db
from application.forms import EntryForm
from application.models import Games, Teams
from flask import render_template, request, redirect, url_for

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_game', methods=['GET', 'POST'])
def add_game():
    form = EntryForm()
    if request.method == "POST":
        game = Games(game_date=form.game_date.data,
        fk_team_name=form.fk_team_name.data,
        home_away=form.home_away.data,
        result=form.result.data,
        points=form.points.data, 
        opponent=form.opponent.data,
        comment=form.comment.data)
        db.session.add(game)
        db.session.commit()
        return redirect(url_for('all_entries'))

    return render_template('add_game.html', form=form)

@app.route('/all_entries')
def all_entries():
    all_games = Games.query.all()
    return render_template('all_entries.html', all_games=all_games)

@app.route('/arsenal_entries')
def arsenal_entries():
    arsenal_games = Games.query.filter_by(fk_team_name='arsenal')
    return render_template('arsenal_entries.html', arsenal_games=arsenal_games)

@app.route('/chelsea_entries')
def chelsea_entries():
    chelsea_games = Games.query.filter_by(fk_team_name='chelsea')
    return render_template('chelsea_entries.html', chelsea_games=chelsea_games)

@app.route('/liverpool_entries')
def liverpool_entries():
    liverpool_games = Games.query.filter_by(fk_team_name='liverpool')
    return render_template('liverpool_entries.html', liverpool_games=liverpool_games)

@app.route('/man_city_entries')
def man_city_entries():
    man_city_games = Games.query.filter_by(fk_team_name='man_city')
    return render_template('man_city_entries.html', man_city_games=man_city_games)

@app.route('/man_utd_entries')
def man_utd_entries():
    man_utd_games = Games.query.filter_by(fk_team_name='man_utd')
    return render_template('man_utd_entries.html', man_utd_games=man_utd_games)

@app.route('/tottenham_entries')
def tottenham_entries():
    tottenham_games = Games.query.filter_by(fk_team_name='tottenham')
    return render_template('tottenham_entries.html', tottenham_games=tottenham_games)

@app.route('/included_entries')
def included_entries():
    ordered_arsenal = Games.query.filter_by(fk_team_name='arsenal', included=True).order_by(Games.game_date.desc()).limit(5)
    ordered_chelsea = Games.query.filter_by(fk_team_name='chelsea', included=True).order_by(Games.game_date.desc()).limit(5)
    ordered_liverpool = Games.query.filter_by(fk_team_name='liverpool', included=True).order_by(Games.game_date.desc()).limit(5)
    ordered_man_city = Games.query.filter_by(fk_team_name='man_city', included=True).order_by(Games.game_date.desc()).limit(5)
    ordered_man_utd = Games.query.filter_by(fk_team_name='man_utd', included=True).order_by(Games.game_date.desc()).limit(5)
    ordered_tottenham = Games.query.filter_by(fk_team_name='tottenham', included=True).order_by(Games.game_date.desc()).limit(5)
    return render_template('included_entries.html', 
    ordered_arsenal=ordered_arsenal,
    ordered_chelsea=ordered_chelsea,
    ordered_liverpool=ordered_liverpool,
    ordered_man_city=ordered_man_city,
    ordered_man_utd=ordered_man_utd,
    ordered_tottenha=ordered_tottenham)


@app.route('/include/<included>/<int:id>')
def include_game(included, id):
    game = Games.query.get(id)
    if included == 'True':
        game.included = True
        db.session.commit()
    elif included == 'False':
        game.included = False
        db.session.commit()
    return redirect(url_for('all_entries'))

@app.route('/delete/<int:id>')
def delete_game(id):
    game = Games.query.get(id)
    db.session.delete(game)
    db.session.commit()
    return redirect(url_for('all_entries'))

@app.route('/team_info')
def team_info():
    all_teams = Teams.query.all()
    return render_template('team_info.html', all_teams=all_teams)


def points(name):
    games = Games.query.filter_by(fk_team_name=name, included=True).order_by(Games.game_date.desc()).limit(5)
    total_points = 0
    for game in games:
        total_points += int(game.points)
    return total_points

@app.route('/table')
def table():
    arsenal = points("arsenal")
    chelsea = points("chelsea")
    liverpool = points("liverpool")
    man_utd = points("man_utd")
    man_city = points("man_city")
    tottenham = points("tottenham")
    return render_template('table.html', arsenal=arsenal, 
    chelsea=chelsea, liverpool=liverpool,
    man_city=man_city, man_utd=man_utd, 
    tottenham=tottenham)












