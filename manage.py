#coding=utf-8
import sys,os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(str(BASE_DIR))
#template manage file

from flask import Flask
from flask_script import Manager

#manage code
from project import create_app

app = create_app()
manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()