# -*- coding=utf-8 -*-

from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user, login_user, logout_user
import jinja2

from ..models import *
from .. import db
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    
    # print("#"*40)
    # for i in Transaction.Transaction.query.all():
    #     print(i.usage)
    # print("#"*40)
    a = Transaction.Transaction.query.all()
    if current_user.is_authenticated:
        try:
            user = User.User.get_user_by_id(current_user.get_id())
            a = user.transaction

        except :
            flash(u"None user")
            return redirect(url_for('main.index'))
        
    print("#"*40)
    for i in CompanyBill.CompanyBill.query.all():
        print(i.date)
    print("#"*40)

    return render_template('main/index.html', list=a)
    # template_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template'))
    # template_env.get_template('base.html')
    # return template_env.render()


@main.route('/read/', methods=['GET', 'POST'])
def read():
    a = request.args.get('trans')       # runturn an unicode
    print("TRANSACTION IN MAIN.ROUTE")
    
    a = Transaction.Transaction.get_transaction_by_id(int(a))
    print(a)
    if a is not None:
        return render_template('main/read.html', a = a)
    flash(u'未找到相关文章')
    return redirect(url_for('main.index'))
