#coding=utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(str(BASE_DIR))
import threading

from flask import current_app, g
from flask.cli import with_appcontext

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

#from ..config import DevelopmentConfig
from .config import Config,DevelopmentConfig

def init_db(app):
    try:
        Config.db = SQLAlchemy()
        try:
             Config.engine = Config.db.create_engine(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
             Config.connection = Config.engine.connect()
        except:
             Config.engine = Config.db.create_engine(DevelopmentConfig.SQLALCHEMY_DATABASE_URI,{})
             Config.connection = Config.engine.connect()
        Config.db.init_app(app)
        
        if not database_exists(DevelopmentConfig.SQLALCHEMY_DATABASE_URI):
            create_database(DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
            record = "database is not existed,init database successfully"
        else:
    	    record = "database existed"
        print(record)
        
        print(database_exists(DevelopmentConfig.SQLALCHEMY_DATABASE_URI))
        if not Config.engine.dialect.has_table(Config.connection, 'Users'):
            print("did not have Users")
            #import module to create table
            from .models.user import UserModel
            with app.app_context():
                Config.db.create_all()
        return Config.db
    except Exception as e:
        print(e)
        print("connect sql failed")
        return False
        
def threading_init_db(app):
    init_db_threading = threading.Thread(target=init_db, args=(app,))
    init_db_threading.start()

def init_app(app):
    init_db_threading = threading.Thread(target=init_db, args=(app,))
    init_db_threading.start()
    
    
        
        