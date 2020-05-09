from flask_restful import Resource, reqparse
from app.models.feeder import FeederModel

class Feeder(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('attempts',
      type=int,
      required=True,
      help="This field cannot be left blank!"
  )

  def get(self, name):
    feeder = FeederModel.find_by_name(name)
    if feeder:
        return feeder.json()
    return {'message': 'Feeder not found'}, 404

  def post(self, name):
    if FeederModel.find_by_name(name):
        return {'message': "A feeder with name '{}' already exists.".format(name)}, 400

    data = Feeder.parser.parse_args()
    feeder = FeederModel(name, **data)
    try:
        feeder.save_to_db()
    except:
        return {"message": "An error occurred creating the feeder."}, 500

    return feeder.json(), 201

  def delete(self, name):
    feeder = FeederModel.find_by_name(name)
    if feeder:
        feeder.delete_from_db()

    return {'message': 'feeder deleted'}

# class FeederList(Resource):
#   def get(self):
#     return {'feeders': list(map(lambda x: x.json(), FeederModel.query.all()))}


# class Feed(Resource):
#   def post(self, name, attempts):
#     if FeederModel.find_by_name(name):
#       data = Feeder.parser.parse_args()
#       feeder = FeederModel(name, **data)      