from flask_restful import Resource, reqparse
from app.models.History import HistoryModel

class History(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('attempts',
      type=int,
      required=True,
      help="This field cannot be left blank!"
  )

  def get(self, name):
    history = HistoryModel.find_by_name(name)
    if history:
        return history.json()
    return {'message': 'History not found'}, 404

  def post(self, name):
    if HistoryModel.find_by_name(name):
        return {'message': "A History with name '{}' already exists.".format(name)}, 400

    data = History.parser.parse_args()
    history = HistoryModel(name, **data)
    try:
        history.save_to_db()
    except:
        return {"message": "An error occurred creating the History."}, 500

    return history.json(), 201

  def delete(self, name):
    history = HistoryModel.find_by_name(name)
    if history:
        history.delete_from_db()

    return {'message': 'History deleted'}

class HistoryList(Resource):
  def get(self):
    return {'history': list(map(lambda x: x.json(), HistoryModel.query.all()))}


# class Feed(Resource):
#   def post(self, name, attempts):
#     if HistoryModel.find_by_name(name):
#       data = History.parser.parse_args()
#       History = HistoryModel(name, **data)      