#coding=utf-8
from .admin import adminbp
from .auth import authbp
from .index import indexbp
# ...

def init_app(app):
    app.register_blueprint(adminbp)
    app.register_blueprint(indexbp)    
    app.register_blueprint(authbp)    

