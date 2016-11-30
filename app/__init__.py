# -*- coding=utf-8 -*-
from flask import Flask, session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager

from config import config

db = SQLAlchemy()

bootstrap = Bootstrap()

login_manager = LoginManager()  #实例化对象
# login_manager.session_protection = 'strong' #设置flask-login session等级
login_manager.login_view = 'admin.login'    #如果未登入转跳到指定方法
login_manager.login_message = u'please login first' #未登入提示语

def create_app(config_name):
    """
    binding extensions to app
    regist blue prients
    """
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config[config_name])
    # config[config_name].init_app(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        
        from init_seed import init_DB_data
        init_DB_data(db)

    bootstrap.init_app(app)
    login_manager.init_app(app)

    from .main import main as main_blueprint
    # print main_blueprint.show()
    app.register_blueprint(main_blueprint)

    from .admin import views
    from .admin import admin as admin_blueprint
    # print(type(admin_blueprint))
    app.register_blueprint(admin_blueprint, url_prefix='/admin')

    return app


