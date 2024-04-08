# Add any model classes for Flask-SQLAlchemy here
import unicodedata
from sqlalchemy import Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime,timezone
from . import db

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(Text)
    poster = Column(String(255))
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))


def __init__(self, movietitle,description,poster, created_at):
    self.movietitle= movietitle
    self.description= description
    self.poster= poster
    self.created_at= created_at

def get_id(self):
        try:
            return unicodedata(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

def __repr__(self):
    return '<Movie %r>' % (self.movietitle)