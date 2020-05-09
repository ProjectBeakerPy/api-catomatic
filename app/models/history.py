from app.db import db 

class HistoryModel(db.Model):
  __tablename__ = 'history'

  history_id = db.Column(db.Integer, primary_key=True)
  attempts = db.Column(db.Integer)
  error_message = db.Column(db.string(500))
  created_date = db.Column(DateTime, default=datetime.datetime.utcnow)

  feeder_id = db.Column(db.Integer, db.ForeignKey('feeder.feeder_id'))
  feeder = db.relationship('FeederModel')

    
  def __init__(self, name, attempts, error_message):
      self.name = name
      self.attempts = attempts
      self.error_message = error_message

  def json(self):
    return { 'name': self.name, 'attempts': self.attempts, 'error_message': self.error_message}

  @classmethod
  def find_by_name(cls, name):
    return cls.query.filter_by(name=name).first()

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()
