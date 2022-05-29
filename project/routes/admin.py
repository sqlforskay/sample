#coding=utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(str(BASE_DIR))
import functools

from flask import (
    Blueprint,flash,g,redirect,render_template,request,session, url_for,current_app,jsonify,abort,send_from_directory
)
from jinja2 import TemplateNotFound
from werkzeug.security import check_password_hash, generate_password_hash

from ..services import external_functions as e_f_m
e_f = e_f_m.external_functions()
external_functions = e_f
from ..services import external_objects as e_o_m
e_o = e_o_m.external_objects()
external_objects = e_o

adminbp = Blueprint('admin', __name__,url_prefix='/admin')

def admin_login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.username is None:
            return redirect("/admin/")
        return view(**kwargs)
    return wrapped_view
    
@adminbp.route('/admin', methods=('GET', 'POST'))
@admin_login_required
def admin():
    return render_template('admin.html',name="sample admin web") 

@adminbp.route('/data', methods=('GET', 'POST'))
@admin_login_required
def data():
    #get data from username
    admin_data = {"name":"sample"}
    return jsonify(admin_data)

@adminbp.route('/', methods=('GET', 'POST'))
def admin_login():
    return render_template('adminlogin.html',name="sample admin_login web")

    
