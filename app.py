import pymysql
from flask import Flask
from api import board
from db_connect import db

app = Flask(__name__)
app.register_blueprint(board)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:devpass@127.0.0.1:3306/anonyboard"

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
# hello