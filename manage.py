# -*-coding:utf-8 -*-
from flask import Flask
from flask_script import Manager, Shell
from app import create_app

app = create_app('default')
app.config['SECRET_KEY'] = 'learn python'
manager = Manager(app)


if __name__ == '__main__':
    app.run(threaded=True, host='192.168.0.171')

