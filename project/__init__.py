#coding=utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(str(BASE_DIR))

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

from flask import Flask
from .config import Config,DevelopmentConfig

def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True,static_url_path='',static_folder='templates')
    print(app.instance_path)
    print(app.config)
    
    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #load config
    #app.config.from_mapping(
    #    SECRET_KEY='dev',
    #   DATABASE=os.path.join(app.instance_path, 'flask.sql'),
    #)
    #print(app.config["DATABASE"])
    #app.config.from_pyfile('config.py', silent=True)
    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
        app.config.from_object(DevelopmentConfig)
        app.config.from_object(Config)
        print("load app config ------------------")
    else:
        app.config.from_mapping(test_config)
        
    Config.app = app
    
    #load extension
    #......
    #from flask_babel import Babel
    #babel = Babel(app)
    
    #init routes, services, file
    #init file
    from . import database
    database.init_app(app)
    #init folder
    from . import routes, services
    routes.init_app(app)
    services.init_app(app)
    
    Config.app = app
    
    return app