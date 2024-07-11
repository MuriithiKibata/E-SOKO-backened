from flask import Flask
from flask_migrate import Migrate
from models import db, User
from flask_restful import Resource, Api
from resources.product import ProductResource
from resources.order import OrderResource


app = Flask(__name__)
api = Api(app)

migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

api.add_resource(ProductResource, '/products', '/products/<int:id>')
api.add_resource(OrderResource, '/orders', '/orders/<int:id>')