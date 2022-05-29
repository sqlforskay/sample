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

from ..services import external_functions as e_f_m
e_f = e_f_m.external_functions()
external_functions = e_f

authbp = Blueprint('auth', __name__,url_prefix='/auth')

@authbp.before_app_request
def load_logged_in_user():
    try:
        username = session['username'] 
    except:
        username = None
    if username is None:
        g.username = None
    else:
        g.username = "username"

@authbp.route('/admin/login', methods=('GET', 'POST'))
def admin_login_post():
    getpostdict = e_f.s_r(request)
    g_p_d = getpostdict
    username = g_p_d['username']
    password = g_p_d['password']
    error = None
    #print(g_p_d)
    if not (username == "sample" and password == "sample"):
        error = u"username or password is not correct"
    if error is None:
        session.clear()
        session['username'] = "admin"
        return redirect("/admin/admin")
    flash(error)
    return "login failed"


