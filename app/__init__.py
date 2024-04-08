from flask import Flask
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import os 

app = Flask(__name__)
app.config.from_object(Config)
#app.config['UPLOAD FOLDER']=os.path.join(os.getcwd())
db=SQLAlchemy
migrate=Migrate(app,db)

from app import views