# -*- coding=utf-8 -*-

from flask import render_template, flash, redirect, url_for, request, make_response, current_app
from flask_login import login_required, current_user, login_user, logout_user
from forms import *
from ..models import *
from .. import db
from ..utils import db_utils 
from . import admin

@admin.route('/')
def index():
    # print("1")
    return render_template('admin/index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    """
    if cookie exists, log in without form
    else give an random one
    """
    form = LoginForm()
    if form.validate_on_submit():
        # print(form.username.data)
        user = User.User.get_user_by_username(form.username.data)
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('admin.index'))
        else:
            flash(u'user do not exist')
        # print user, form.password.data
        flash(u'log in faild')
    return render_template('admin/login.html', form=form)


@admin.route('/register', methods=['GET', 'POST'])
def register():
    # register_key = 'zhucema'
    form = RegistrationForm()
    if form.validate_on_submit() and not User.User.isUserExist(form.username.data):
        # if form.registerkey.data != register_key:
        #     flash(u'注册码不符,请返回重试.')
        #     return redirect(url_for('admin.register'))
        # else:
        if form.password.data != form.password2.data:
            flash(u'两次输入密码不一')
            return redirect(url_for('admin.register'))
        else:
            user = User.User()
            user.username=form.username.data 
            user.real_name=form.real_name.data
            user.password=form.password.data
            db_utils.commit_data(db, user)
            # print(user.username)
            flash(u'您已经注册成功')
            return redirect(url_for('admin.login'))
    return render_template('admin/register.html', form=form)


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'您已经登出了系统')
    redirect_to_index = redirect(url_for('main.index'))
    response = current_app.make_response(redirect_to_index )  
    response.set_cookie('USERID',value="GUEST")
    return response
    


@admin.route('/transaction', methods=['GET', 'POST'])
@login_required
def transaction_modify():
    
    user = db.session.query(User.User).filter(User.User.id == current_user.get_id()).first()

    # print(a)
    
    
    if user:
        wallet = user.wallet
        trans_instance = user.transaction
        alist = user.transaction
        # print(user.username)
        # print(alist)
    else:
        flash("ERROR: can not find user")
        redirect(url_for('admin.index'))
    form = PostTransactionForm()
    

    if form.validate_on_submit():
        if form.payment.data != None :
            if form.payment.data == 'wallet':
                if form.wallet.data != None and form.wallet.data != 0:
                    user.pay_trans(trans=trans_instance, number = form.wallet.data)
                # else:
                #     flash(u'nothing in wallet! use bank card instead!')
                    # redirect(url_for('admin.transaction'))
            elif form.payment.data == 'bank_card':
                if form.bank_card.data != None and form.bank_card.data != 0:
                    user.pay_trans(trans=trans_instance, number = form.bank_card.data)

        db.session.commit()
        flash(u'pay successful')
        return redirect(url_for('admin.index'))
    return render_template('admin/pay.html', form=form, list=alist)


@admin.route('/transaction/del', methods=['GET', 'POST'])
@login_required
def transaction_refund():
    user = db.session.query(User.User).filter(User.User.id == current_user.get_id()).first()

    # print(a)
    if user:
        wallet = user.wallet
        # trans_instance = user.transaction
        bill_list = user.bank_bill_item
        # print(user.username)
        # print(alist)
    else:
        flash("ERROR: can not find user")
        return redirect(url_for('admin.index'))
    form = PostTransactionReFundForm()
    

    if form.validate_on_submit():

        if form.serial_number.data != None:
            flag = user.refund_trans(serial_number=int(form.serial_number.data))
        else:
            flash(u'choose one serial_number first')
            return redirect(url_for('admin.index'))
        db.session.commit()
        if flag:
            flash(u'refund successful')
            # return redirect(url_for('admin.transaction_refund'))
    return render_template('admin/refund.html', form=form, list=bill_list)

@admin.route('/check', methods=['GET', 'POST'])
@login_required
def check():
    cost = BankBill.BankBillItem.get_total_money_in_date()
    num = BankBill.BankBillItem.get_total_trans_number_in_date()
    date = BankBill.BankBillItem.get_date()
    bill_list = db.session.query(BankBill.BankBillItem).all()
    return render_template('admin/check.html', cost = cost, number = num, data = date, list=bill_list)
# @admin.route('/category', methods=['GET', 'POST'])
# def category():
#     clist = Category.query.all()
#     form = PostCategoryForm()
#     if form.validate_on_submit():
#         category = Category(name=form.name.data)
#         db.session.add(category)
#         flash(u'分类添加成功')
#         return redirect(url_for('admin.index'))
#     return render_template('admin/category.html', form=form, list=clist)


# @admin.route('/category/del', methods=['GET'])
# @login_required
# def category_del():
#     if request.args.get('id') is not None and request.args.get('a') == 'del':
#         x = Category.query.filter_by(id=request.args.get('id')).first()
#         if x is not None:
#             db.session.delete(x)
#             db.session.commit()
#             flash(u'已经删除' + x.name)
#             return redirect(url_for('admin.category'))
#         flash(u'请检查输入')
        # return redirect(url_for('admin.category'))
