from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from config import Config

from app.security import authenticate, identity
from app.resources.user import UserRegister
from app.resources.item import Item, ItemList
from app.resources.store import Store, StoreList
from app.db import db 

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app) 
jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')

api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')

api.add_resource(UserRegister, '/register')

@app.before_first_request
def create_tables():
  db.create_all()

db.init_app(app)