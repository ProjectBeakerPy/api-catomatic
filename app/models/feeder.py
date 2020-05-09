from app.db import db 

class FeederModel(db.Model):
  __tablename__ = 'feeder'

  feeder_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80))
  attempts = db.Column(db.Integer)

    
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
