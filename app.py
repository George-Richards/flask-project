from application import app, db
from flask import Flask


db.create_all()


if __name__ =='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

