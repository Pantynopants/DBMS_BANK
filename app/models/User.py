# -*- coding=utf-8 -*-

from .. import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin 
import hashlib

import Transaction
SALT = "@#3k25l23#KW#LRsekr@#"


# tags = db.Table('tags',
#                 db.Column('category_id', db.Integer, db.ForeignKey('category.id')),
#                 db.Column('article_id', db.Integer, db.ForeignKey('article.id')),
#                 db.PrimaryKeyConstraint('category_id', 'article_id')
#                 )


# class Category(db.Model):
#     # __tablename__ = 'categorys'
#     __table_args__ = {'extend_existing': True}
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String(64), unique=True)
#     article = db.relationship('Article', secondary=tags, backref=db.backref('categorys'))
#     def __init__(self, **args):
#         if (len(args) > 2):
#             print("wrong args number")
#             return
#         self.__dict__.update(args)


class User(UserMixin, db.Model):
    r"""when using Flask-Login , user model need succeed UserMimix
    """

    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)        # nick name
    # password_hash = db.Column(db.String(256))
    # user_cookies = db.Column(db.Text)
    real_name = db.Column(db.String(64), unique=True)
    # article = db.relationship('Article', backref=db.backref('users'))

    # id_bank_account = db.Column(db.Integer, db.ForeignKey('bank_account.id'))
    db.relationship('BankAccount', backref=db.backref('users'))
    db.relationship('transaction', backref=db.backref('users'))
    db.relationship('CompanyBill', backref=db.backref('users'))
    db.relationship('Equipment', backref=db.backref('users'))

    # id_transaction = db.Column(db.Integer, db.ForeignKey('transaction.id'))

    wallet = db.Column(db.Float)
    # @property
    # def password(self):
    #     raise AttributeError('password is a private attrubute')

    # @password.setter
    # def password(self, password):
    #     # self.password_hash = generate_password_hash(password)
    #     # 增加password会通过generate_password_hash方法来加密储存
    #     self.password_hash = bcrypt.hashpw(password, bcrypt.gensalt())


    # def verify_password(self, password):
    #     # return check_password_hash(self.password_hash, password)
    #     # 在登入时,我们需要验证明文密码是否和加密密码所吻合
    #     return bcrypt.hashpw(password, self.password_hash) == self.password_hash


    # helper functions
    


    def __init__(self, **args):
        if (len(args) > 5):
            print("wrong args number")
            return
        super(User, self).__init__(**args)
        # self.makeCookie(args['username'])
        # if "password" in args.keys():
        #     self.password = str(args["password"])

    @classmethod
    def get_users(self):
        users = db.session.query(User).all()
        return users
    
    
    @classmethod
    def get_user_by_id(self, user_id):
        user = db.session.query(User).filter(User.id == user_id).first()
        return user

    @classmethod
    def get_user_by_expression(self, expression):
        """
        expression: str
        """
        user = db.session.query(User).filter(eval(expression)).first()
        return user


    @classmethod
    def get_trans_by_user_id(self, user_id):
        try:
            trans = db.session.query(Transaction.Transaction).filter(Transaction.Transaction.user_name == user_id).first()
        except Exception, e:
            raise e
        
        return trans



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#################################


        







