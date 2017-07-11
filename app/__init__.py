# -*-coding:utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
import pymysql
from config import config


bootstrap = Bootstrap()
print()
connection = pymysql.connect(host='localhost', user='root', password='',
                             database='duan', port=3306, charset='utf8')


def create_app(config_name):
    app = Flask(__name__, static_folder='static', template_folder='templates')
    # app.config.from_object(config[config_name])
    bootstrap.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app
