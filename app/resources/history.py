from flask_restful import Resource
from app.models.history import HistoryModel

class History(Resource):
  def get(self, history_id):
    history = HistoryModel.find_by_history_id(history_id)
    if history:
        return history.json()
    return {'message': 'History not found'}, 404

  def delete(self, history_id):
    history = HistoryModel.find_by_history_id(history_id)
    if history:
        history.delete_from_db()

    return {'message': 'History deleted'}

class HistoryList(Resource):
  def get(self):
    return {'history': list(map(lambda x: x.json(), HistoryModel.query.all()))}
