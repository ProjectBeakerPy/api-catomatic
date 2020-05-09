from app.db import db 

class HistoryModel(db.Model):
  __tablename__ = 'history'

  history_id = db.Column(db.Integer, primary_key=True)

  feeder_id = db.Column(db.Integer, db.ForeignKey('feeder.feeder_id'))
  feeder = db.relationship('FeederModel')

    
  def __init__(self, name, attempts):
      self.name = name
      self.attempts = attempts

  def json(self):
    return { 'name': self.name, 'attempts': self.attempts}

  @classmethod
  def find_by_name(cls, name):
    return cls.query.filter_by(name=name).first()

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()
