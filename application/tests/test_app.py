from flask_testing import TestCase
from application import app, db
from application.models import Games
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///test-db', DEBUG=True, WTF_CSRF_ENABLED=False)
        return app

    def setUp(self):
        db.create_all()
        game1 = Games(fk_team_name="Test", home_away="Test", result="Test", points="Test", opponent="Test", comment="Test", included=True)
        game2 = Games(fk_team_name="Demo", home_away="Demo", result="Demo", points="Demo", opponent="Demo", comment="Demo", included=True)
        db.session.add(game1)
        db.session.add(game2)
        db.session.commit()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    
class TestResponse(TestBase):
    def test_add_game_get(self):
        response = self.client.get(url_for('add_game'))
        self.assertEqual(response.status_code, 200)
    def test_all_entries_get(self):
        response = self.client.get(url_for('all_entries'))
        self.assertEqual(response.status_code, 200)
    def test_arsenal_entries_get(self):
        response = self.client.get(url_for('arsenal_entries'))
        self.assertEqual(response.status_code, 200)
    def test_chelsea_entries_get(self):
        response = self.client.get(url_for('chelsea_entries'))
        self.assertEqual(response.status_code, 200)
    def test_included_entries_get(self):
        response = self.client.get(url_for('included_entries'))
        self.assertEqual(response.status_code, 200)
    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
    def test_liverpool_entries_get(self):
        response = self.client.get(url_for('liverpool_entries'))
        self.assertEqual(response.status_code, 200)
    def test_man_city_entries_get(self):
        response = self.client.get(url_for('man_city_entries'))
        self.assertEqual(response.status_code, 200)
    def test_man_utd_entries_get(self):
        response = self.client.get(url_for('man_utd_entries'))
        self.assertEqual(response.status_code, 200)
    def test_table_get(self):
        response = self.client.get(url_for('table'))
        self.assertEqual(response.status_code, 200)
    def test_team_info_get(self):
        response = self.client.get(url_for('team_info'))
        self.assertEqual(response.status_code, 200)
    def test_tottenham_entries_get(self):
        response = self.client.get(url_for('tottenham_entries'))
        self.assertEqual(response.status_code, 200)

class TestAdd(TestBase):
    def test_add_game(self):
        with self.client:
            response = self.client.post('/add_game',
            data = dict(fk_team_name="Test1", 
            home_away="Test", 
            result="Test", 
            points="Test", 
            opponent="Test", 
            comment="Test", 
            included=True), 
            follow_redirects=True
        )
        self.assertIn(b'Test1', response.data)

