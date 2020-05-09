from app.db import db
import datetime
import time
import sys
# import RPi.GPIO as GPIO
from sqlalchemy import Column, Integer, DateTime, String, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class FeederModel(db.Model):
  __tablename__ = 'feeder'

  feeder_id = Column(Integer, primary_key=True)
  name = Column(String(80))
  attempts = Column(Integer)
  is_active = Column(Boolean, default=True)
  created_date = Column(DateTime, default=datetime.datetime.utcnow)

  def __init__(self, name, attempts):
      self.name = name
      self.attempts = attempts

  def json(self):
    return { 
      'feeder_id': self.feeder_id,
      'name': self.name,
      'attempts': self.attempts,
      'created_date': str(self.created_date)
    }

  @classmethod
  def feed(cls, attempts):
    try: 
      ## This is where the catomatic logic will go.      
      return True
    except:
      return False

  @classmethod
  def find_by_name(cls, name):
    return cls.query.filter_by(name=name).first()

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()
