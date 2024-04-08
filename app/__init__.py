from flask import Flask
from .config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect 
import os 

app = Flask(__name__)
app.config.from_object(Config)
csrf = CSRFProtect(app)
#app.config['UPLOAD FOLDER']=os.path.join(os.getcwd())
db=SQLAlchemy
migrate=Migrate(app,db)

from app import views