# -*- coding=utf-8 -*-
from flask_wtf import FlaskForm as Form
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, FloatField, SelectField
from wtforms.validators import Required, length, Regexp, EqualTo
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import *

class LoginForm(Form):
    username = StringField(u'帐号', validators=[Required(), length(6, 64)])
    password = PasswordField(u'密码', validators=[Required()])
    submit = SubmitField(u'登入')

class CookieLoginForm(Form):
    username = StringField(u'帐号', validators=[Required(), length(6, 64)])
    real_name = StringField(u'密码', validators=[Required()])
    submit = SubmitField(u'登入')

class RegistrationForm(Form):
    username = StringField(u'用户名',
        validators=[Required(),
        length(6, 18)
        # , Regexp(r'^[0-9_.]*$', 'please do not use special symbol')
        ])
    password = PasswordField(
        u'密码', validators=[Required(), EqualTo('password2', message=u'密码错误提示1')])
    password2 = PasswordField(u'重复密码', validators=[Required()])
    real_name = StringField(u'昵称', validators=[Required()])
    # registerkey = StringField(u'注册码', validators=[Required()])
    submit = SubmitField(u'注册')


class PostArticleForm(Form):
    title = StringField(u'标题', validators=[Required(), length(6, 64)])
    body = TextAreaField(u'内容')
    category_id = QuerySelectField(u'分类',
        # query_factory = lambda: Category.query.all(),
        query_factory = lambda: [],
        get_pk = lambda a: str(a.id),
        get_label=lambda a: a.name)
    submit = SubmitField(u'发布')


class PostCategoryForm(Form):
    name = StringField(u'分类名', validators=[Required(), length(6, 64)])
    submit = SubmitField(u'发布')



class PostTransactionForm(Form):
    payment = SelectField(u'payment', choices=[('wallet', 'wallet'), ('bank_card', 'bank_card')])
    wallet = FloatField(u'wallet')

    bank_card = FloatField(u'bank_card')
    

    submit = SubmitField(u'pay')

    def __init__(self, default = None, **arg):
        super(User, self).__init__(**args)
        self.wallet = FloatField(u'wallet', default = default)


        