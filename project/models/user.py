# coding=utf-8
from ..services import external_functions as e_f_m
e_f = e_f_m.external_functions()
external_functions = e_f
from ..services import external_objects as e_o_m
e_o = e_o_m.external_objects()
external_objects = e_o

from ..config import Config,DevelopmentConfig

db = Config.db

class UserModel(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))
    registrationtime = db.Column(db.String(120))
    registrationip = db.Column(db.String(120))
     
    def __init__(self, name=None, email=None,password=None,registrationip=None):
        self.name = name
        self.email =  email
        self.password = password
        self.registrationtime = str(e_f.get_time())
        self.registrationip = registrationip