from app.db import db
import datetime
from sqlalchemy import ( Column, 
                       Integer, 
                       DateTime, 
                       String, 
                       desc, 
                       ForeignKey
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class HistoryModel(db.Model):
  __tablename__ = 'history'

  history_id = Column(Integer, primary_key=True)
  attempts = Column(Integer)
  error_message = Column(String(500))
  created_date = Column(DateTime, default=datetime.datetime.utcnow)

  feeder_id = Column(Integer, ForeignKey('feeder.feeder_id'))
  feeder = relationship('FeederModel')

    
  def __init__(self, feeder_id, attempts, error_message=None):
      self.feeder_id = feeder_id
      self.attempts = attempts
      self.error_message = error_message

  def json(self):
    return { 
      'history_id': self.history_id,
      'feeder_id': self.feeder_id,
      'attempts': self.attempts,
      'error_message': self.error_message,
      'created_date': str(self.created_date)
    }

  @classmethod
  def find_by_history_id(cls, history_id):
    return cls.query.filter_by(history_id=history_id).first()

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()
