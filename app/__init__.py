from flask import Flask
from flask_restful import Api
from config import Config


from app.resources.feeder import Feeder, FeederList, Feed
from app.resources.history import History, HistoryList
from app.resources.healthcheck import HealthCheck
from app.db import db 

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app) 

api.add_resource(HealthCheck, '/healthcheck')

api.add_resource(Feeder, '/feeder/<string:name>')
api.add_resource(FeederList, '/feeders')
api.add_resource(Feed, '/feed/<string:name>')

api.add_resource(History, '/history/<int:history_id>')
api.add_resource(HistoryList, '/history')

@app.before_first_request
def create_tables():
  db.create_all()

db.init_app(app)