from flask import Flask
from flask_restful import Api
from config import Config

# from app.resources.item import Item, ItemList
# from app.resources.store import Store, StoreList
from app.db import db 

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app) 

# api.add_resource(Item, '/item/<string:name>')
# api.add_resource(ItemList, '/items')

# api.add_resource(Store, '/store/<string:name>')
# api.add_resource(StoreList, '/stores')

api.add_resource(Feeder, '/feeder/<string:name>')
# api.add_resource(FeederList, '/feeders')
# api.add_resource(Feed, '/feed/<string:name>')
# api.add_resource(History, '/history/<string:name>')
# api.add_resource(HistoryList, '/history')

@app.before_first_request
def create_tables():
  db.create_all()

db.init_app(app)