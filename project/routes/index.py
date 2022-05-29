#coding=utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(str(BASE_DIR))

import functools,datetime,random,string,json

import requests

from flask import (
    Blueprint,flash,g,redirect,render_template,request,session, url_for,current_app,jsonify,abort,send_from_directory
)
from jinja2 import TemplateNotFound
from werkzeug.security import check_password_hash, generate_password_hash

#from ..config import DevelopmentConfig
from ..config import Config,DevelopmentConfig

from ..services import external_functions as e_f_m
e_f = e_f_m.external_functions()
external_functions = e_f
from ..services import external_objects as e_o_m
e_o = e_o_m.external_objects()
external_objects = e_o

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine,exc
from sqlalchemy_utils import database_exists, create_database

from .. import database
from ..models.user import UserModel

indexbp = Blueprint('', __name__,url_prefix='/')
@indexbp.route('/init', methods=('GET', 'POST'))
def init():
    try:
        database.threading_init_db(Config.app)
        return "inited"
    except Exception as e:
        print(e)
        return "error: " + str(e)
        
#set up icon
@indexbp.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('favicon.ico')
            
@indexbp.route('/', methods=('GET', 'POST'))
def index():
    getpostdict = e_f.s_r(request)
    g_p_d = getpostdict
    #print(g_p_d)
    #return render_template('index.html',name="sample index")
    return "hello sample flask"

@indexbp.route('/test/sample', methods=('GET', 'POST'))
def tese_sample():
    getpostdict = e_f.s_r(request)
    g_p_d = getpostdict
    serial = e_f.g_s()
    g_p_d['serial'] = serial
    g_p_d['ip'] = request.remote_addr
    g_p_d['time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    print(UserModel.query.all())
    try:
        Config.db.session.add(UserModel(name="sample", email="sample@sample.com",password="sample@sample.com",registrationip=g_p_d['ip']))
        Config.db.session.commit()
    except exc.IntegrityError as e:
        print(e)
    return "hello sample"
    #return render_template('sample.html',sample=serial)