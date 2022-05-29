#coding=utf-8
import os 

class Config(object):
    DEBUG = False
    TESTING = False
    
    #global object
    db = None
    engine = None
    connection = None
    app = None
    config = None
    
    #global json object
    #key value
    data_template = {"json_data":"json dictionary"}
    template = {"json_data":"json dictionary"}

    # mail settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 25

    # mail authentication
    MAIL_USERNAME = 'bababa'
    MAIL_PASSWORD = 'bababa'

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True

    # session
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(24)

    # datebase
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'sample'
    USERNAME = 'root'
    PASSWORD = 'kali'

    URL = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
    SQLALCHEMY_DATABASE_URI = URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
     

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}