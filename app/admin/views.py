# -*- coding=utf-8 -*-

from flask import render_template, flash, redirect, url_for, request, make_response, current_app
from flask_login import login_required, current_user, login_user, logout_user
from forms import *
from ..models import *
from .. import db
from ..utils import db_utils as Utils
from . import admin

@admin.route('/')
def index():
    print("1")
    return render_template('admin/index.html')


@admin.route('/login', methods=['GET', 'POST'])
def login():
    """
    if cookie exists, log in without form
    else give an random one
    """
    # user = User.query.filter(User.username == form.username.data).first()
    flag, user = Utils.vaildation_user(request)
    form = CookieLoginForm()
    if flag:
        login_user(user)
        return redirect(request.args.get('next') or url_for('admin.index'))
    else:
        
        if form.validate_on_submit():
            if form.username.data is not None and not Utils.isUserExist(form.username.data):
                user = User(username=form.username.data, real_name=form.real_name.data)
                Utils.commit_data(db, user)
                print(user.id)
                flash(u'您已经注册成功')
                login_user(user)
                
                redirect_to_index = redirect(request.args.get('next') or url_for('admin.index'))
                response = current_app.make_response(redirect_to_index )  
                response.set_cookie('USERID',value=form.username.data)
                return response
            flash(u'user already exists')

    return render_template('admin/login.html', form=form)


# @admin.route('/register', methods=['GET', 'POST'])
# def register():
#     register_key = 'zhucema'
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         if form.registerkey.data != register_key:
#             flash(u'注册码不符,请返回重试.')
#             return redirect(url_for('admin.register'))
#         else:
#             if form.password.data != form.password2.data:
#                 flash(u'两次输入密码不一')
#                 return redirect(url_for('admin.register'))
#             else:
#                 user = User(username=form.username.data, password=form.password.data, real_name=form.real_name.data)
#                 from ..Utils import commit_data
#                 commit_data(db, user)
#                 print(user.id)
#                 flash(u'您已经注册成功')
#                 return redirect(url_for('admin.login'))
#     return render_template('admin/register.html', form=form)


@admin.route('/logout')
@login_required
def logout():
    logout_user()
    flash(u'您已经登出了系统')
    redirect_to_index = redirect(url_for('main.index'))
    response = current_app.make_response(redirect_to_index )  
    response.set_cookie('USERID',value="GUEST")
    return response
    


# @admin.route('/article', methods=['GET', 'POST'])
# @login_required
# def article():
#     form = PostArticleForm()
#     alist = Article.query.all()
#     if form.validate_on_submit():
#         acticle = Article(title=form.title.data, body=form.body.data, category_id=str(form.category_id.data.id),
#                           user_id=current_user.id)
#         db.session.add(acticle)
#         flash(u'文章添加成功')
#         redirect(url_for('admin.index'))
#     return render_template('admin/article.html', form=form, list=alist)


# @admin.route('/article/del', methods=['GET'])
# @login_required
# def article_del():
#     if request.args.get('id') is not None and request.args.get('a') == 'del':
#         x = Article.query.filter_by(id=request.args.get('id')).first()
#         if x is not None:
#             db.session.delete(x)
#             db.session.commit()
#             flash(u'已经删除' + x.title)
#             return redirect(url_for('admin.article'))
#         flash(u'请检查输入')
#         return redirect(url_for('admin.article'))


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
