from flask_restful import Resource, reqparse
from models import db, Cart

class CartResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('product', type=int, required=True, help="item is required")
    parser.add_argument('')
