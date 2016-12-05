# -*- coding=utf-8 -*-

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user, login_user, logout_user
import jinja2

from ..models import *
from .. import db
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    
    a = Transaction.Transaction.query.all()
    return render_template('main/index.html', list=a)
    # template_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))
    # template_env.get_template('base.html')
    # return template_env.render()


@main.route('/read/', methods=['GET', 'POST'])
def read():
    a = request.args.get('trans')       # runturn an unicode
    # print(a)
    a = Transaction.Transaction.get_transaction_by_id(int(a))
    if a is not None:
        return render_template('main/read.html', a = a)
    flash(u'未找到相关文章')
    return redirect(url_for('main.index'))
