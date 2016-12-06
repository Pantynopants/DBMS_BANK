# -*- coding=utf-8 -*-

from .. import db
from ..utils import db_utils
import Transaction
import CompanyBill
class Clerk(db.Model):
    __tablename__ = 'clerk'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # id_transaction = db.Column(db.Integer, db.ForeignKey("transaction.id", onupdate="CASCADE", ondelete="CASCADE"))
    # equipment = db.relationship('Equipment', backref=db.backref('clerk'))
    equipment_id = db.relationship(
        'Transaction' 
        # ,secondary = Transaction.Transaction
        ,backref=db.backref('clerks', lazy='joined', uselist=False)
        # ,primaryjoin = "Clerk.id==Transaction.transaction.c.clerk_id"
        ,foreign_keys=[Transaction.Transaction.clerk_id]
        )

    def __init__(self, **args):
        if (len(args) > 2):
            print("wrong args number")
            return
        self.__dict__.update(args)

    @classmethod
    def get_clerks(self):
        clerks = db.session.query(Clerk).all()
        return clerks
    
    
    @classmethod
    def get_clerk_by_id(self, clerk_id):
        clerk = db.session.query(Clerk).filter(Clerk.id == clerk_id).first()
        return clerk

    @classmethod
    def get_clerk_by_expression(self, expression):
        """
        expression: str
        """
        clerk = db.session.query(Clerk).filter(eval(expression)).first()
        return clerk

    @staticmethod
    def check_usage_to_trans(user, clerks, equipments, usage):
        # c1.equipments = [e1, e2]
        t1 = Transaction.Transaction()
        t1.users = user
        # u1.transaction = t1
        if user.transaction == None:
            user.transaction = [t1]
        else:
            user.transaction.append(t1)
        t1.user_name = user.real_name
        t1.equipments = equipments
        # print type(equipments)
        t1.clerks = clerks
        t1.usage = usage
        Clerk.add_to_company_bill(t1.users, t1.date, t1.usage, t1)
        return t1

    @staticmethod
    def add_to_company_bill(user, date, money, trans=None):
        comp1 = CompanyBill.CompanyBill(date = date, money = money)
        comp1.users = user
        comp1.transaction = trans
        db_utils.commit_data(db, comp1)
        return comp1
