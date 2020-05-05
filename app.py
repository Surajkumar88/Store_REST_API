import os

from flask import Flask
from flask_restful import Api #a resource is anything that the API is concerned with
from flask_jwt import JWT
from datetime import timedelta

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app  = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')  #if first one is not found, 2nd will be used
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'yahoo'
api = Api(app)

app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=1)
jwt = JWT(app, authenticate, identity)   #jwt creates a new endpoint called /auth

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(port=5000, debug=True)
