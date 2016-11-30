# -*- coding=utf-8 -*-
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from flask import render_template, redirect, url_for, flash, request, session
from datetime import timedelta

from app import create_app, db
from app.models import *

app = create_app('default')
app.debug = True


manager = Manager(app)

migrate = Migrate(app, db)  #注册migrate到flask

manager.add_command('db', MigrateCommand)   #在终端环境下添加一个db命令

@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)

@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=120)

if __name__ == '__main__':

    manager.run()

"""
# first time run you should do:
python manage.py db init
# after change the DB model u should do:
python manage.py db migrate -m "first init db"
python manage.py db upgrade

# always run:
python manage.py runserver
"""

