# -*- coding=utf-8 -*-

from .. import db, login_manager
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin 
import hashlib
import bcrypt
import random

import Transaction,BankBill,Clerk,CompanyBill
from ..utils import deco_utils
from ..utils import db_utils




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

    attributes(backref collection)
    ---------------------------------
    transaction
    bank_bill_item
    """

    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), unique=True)        # nick name
    password_hash = db.Column(db.String(256))
    user_cookies = db.Column(db.Text)
    real_name = db.Column(db.String(64), unique=True)
    # article = db.relationship('Article', backref=db.backref('users'))

    # id_bank_account = db.Column(db.Integer, db.ForeignKey('bank_account.id'))
    db.relationship('BankAccount', backref=db.backref('users', uselist=False))

    db.relationship('transaction', backref=db.backref('users', uselist=False))

    db.relationship('CompanyBill', backref=db.backref('users', uselist=False))

    bank_bill_items = db.relationship('BankBillItem', backref=db.backref('users', uselist=False))

    db.relationship('Equipment', backref=db.backref('users', uselist=False))

    # id_transaction = db.Column(db.Integer, db.ForeignKey('transaction.id'))

    wallet = db.Column(db.Float)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        print("set password")
        self.password_hash = generate_password_hash(password)
        # 增加password会通过generate_password_hash方法来加密储存

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    # helper functions
    


    def __init__(self, **args):
        if (len(args) > 10):
            print("wrong args number")
            return
        super(User, self).__init__(**args)
        # self.makeCookie(args['username'])
        # if "password" in args.keys():
        #     self.password = str(args["password"])

    @classmethod
    def get_users(self):
        """
        Return
        --------
        list
        """
        users = db.session.query(User).all()
        return users
    
    
    @classmethod
    def get_user_by_id(self, user_id):
        user = db.session.query(User).filter(User.id == user_id).first()
        return user

    @classmethod
    def get_user_by_username(self, username):
        user = db.session.query(User).filter(User.username == username).first()
        return user

    @classmethod
    def get_user_by_expression(self, expression):
        """
        expression: str
        """
        user = db.session.query(User).filter(eval(expression)).first()
        return user

    # @classmethod
    # must use as instance, since User is a model
    # after instance, user has the attribute: transaction
    def get_my_trans(self):
        # return self.transaction.query.all()
        return self.transaction

    @classmethod
    def get_trans_by_user_id(self, user_name):
        try:
            trans = db.session.query(Transaction.Transaction).filter(Transaction.Transaction.user_name == user_name).first()
        except Exception, e:
            raise e
        
        return trans

    # @classmethod
    @deco_utils.vaildation_parameter
    def set_trans_usage(self, trans, number):
        """
        Parameter
        ----------
        Transaction(1 row), int/float
        """
        trans.usage -= number
        date_now = datetime.utcnow()
        my_bank_log = User.get_my_bank_bill_items(self.real_name)
        # print("#"*40)
        # print(my_bank_log, type(my_bank_log))
        # print("#"*40)
        bill = BankBill.BankBillItem(
            id_user = self
            , user_name = self.real_name
            , exchange = number
            , date = date_now
            , serial_number = random.randint(1000, 9999)
            , bank = 1
            )
        if my_bank_log == None:
            my_bank_log = []
        my_bank_log.append(bill)
        self.bank_bill_items = my_bank_log
        # db_utils.commit_data(db, self)
        print(self.bank_bill_items)
        Clerk.Clerk.add_to_company_bill(user=self, date=date_now, money = number, trans = trans)
        return trans

    @classmethod
    def get_bank_bill_items(self):
        return db.session.query(BankBill.BankBillItem).all()

    @staticmethod
    def get_my_bank_bill_items(my_username):
        return db.session.query(BankBill.BankBillItem).filter(BankBill.BankBillItem.user_name == my_username).all()
        # return db.session.query(BankBill.BankBillItem).filter(BankBill.BankBillItem.id_user == self).first()

    # @classmethod
    @deco_utils.vaildation_parameter
    def pay_trans(self, trans=[], number=0):
        """specific all parameters, if None, use [] instead
        """
        pay_money = number
        if len(trans) == 0:
            trans = self.get_my_trans()
        print(type(trans))

        if len(trans) >= 0:
            #TODO
            # modify trans by date
            for i in trans:
                # print(pay_money)
                if i.usage<=0:
                    continue
                if i.usage <= pay_money:
                    pay_money -= i.usage
                    self.set_trans_usage(trans=i, number=i.usage)
                    
                else:
                    self.set_trans_usage(trans=i, number=pay_money)
                    
                    break
        else:
            self.set_trans_usage(trans=trans[0], number=number)
        print("success")

    @deco_utils.vaildation_parameter
    def refund_trans(self, serial_number=None, number=0):
        bank_bill = BankBill.BankBillItem.query.filter(BankBill.BankBillItem.serial_number == serial_number).first()
        if bank_bill == None:
            print("can not find this transaction: No such serial_number")
            return
        company_bill = CompanyBill.CompanyBill.query.filter(CompanyBill.CompanyBill.date == bank_bill.date).first()
        if company_bill == None:
            print("can not find this transaction: No such record in company")
            return
        self.set_trans_usage(trans=company_bill.transaction, number=company_bill.money*(-1))

    @staticmethod
    def submit_company(user_id = None, date = None, money = 0):
        """
        add one row to company bill
        """
        db_utils.commit_data(db, CompanyBill.CompanyBill(id_user = user_id, date = date, money = money))
        return True

    @staticmethod
    def isUserExist(name):   
        """
        exist:return true
        """
        return User.query.filter(User.username == name).count() != 0

    @staticmethod
    def vaildation_user(request):
        """
        para:
            request(Flask.request)
        return:
            True, user(Model.User)
            or
            False, None

        """
        cookie = request.cookies.get('USERID', 'GUEST')
        (userid, hashed) = db_utils.parseCookie(cookie)
        user = User.query.filter(User.username == userid).first()
        # suc_message = "admin log in"
        # ordinary_message = "user log in"
        # norm_message = "guest log in"
        
        # if isUserAwesome(userid) and isCookieValid(cookie):
        #     resp = make_response(suc_message)
        #     resp.set_cookie("USERID", makeCookie("administrator"))
        if User.isUserExist(userid) and db_utils.isCookieValid(cookie) and user is not None and userid != "GUEST":
            return True, user
            # resp = make_response(ordinary_message)
            # user = User.query.filter(User.username == name).first()

            # resp.set_cookie("USERID", user.user_cookies)
        else:
            return False, user
            # resp = make_response(norm_message)
            # resp.set_cookie("USERID", makeCookie("GUEST"))
        # return resp



@login_manager.user_loader
def load_user(user_id):
    if user_id is None or user_id == 'None': 
       user_id =-1
    print 'ID: %s, leaving load_user' % (user_id)
    return User.query.get(int(user_id))

#################################


        







