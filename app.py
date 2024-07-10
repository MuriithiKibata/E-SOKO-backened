from flask import Flask
from flask_migrate import Migrate
from models import db, User


app = Flask(__name__)

migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)