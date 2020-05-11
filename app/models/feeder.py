from app.db import db
import datetime
import time
import sys
import RPi.GPIO as GPIO
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
    # return True 
    # If you need to run this locally, then comment out the gpio and the rest of this method, it wont work on windows. 
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    try: 
      ## This is where the catomatic logic will go.
      servo = GPIO.PWM(12, 50)
      servo.start(12.5)

      # spin left, right, then left again rather than in a continuous circle
      # to prevent the food from jamming the servo
      for index in range(0, attempts):
          dutyCycle = 2.5 if (index % 2 == 0) else 12.5
          servo.ChangeDutyCycle(dutyCycle)
          # adjust the sleep time to have the servo spin longer or shorter in that direction
          time.sleep(.75)     
    except:
      return False
    finally:
        # always cleanup after ourselves
        servo.stop()
        GPIO.cleanup()
        return True

  @classmethod
  def find_by_name(cls, name):
    return cls.query.filter_by(name=name).first()

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  def delete_from_db(self):
    db.session.delete(self)
    db.session.commit()
