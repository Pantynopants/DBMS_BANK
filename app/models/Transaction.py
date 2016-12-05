# -*- coding=utf-8 -*-
from datetime import datetime
from .. import db
from ..utils import db_utils
import CompanyBill
# Transaction = db.Table('transaction'
#                 ,db.Column('id', db.Integer, primary_key=True, autoincrement=True)
#                 ,db.Column('clerk_id', db.Integer, db.ForeignKey('clerk.id'), primary_key=True)
#                 ,db.Column('equipment_id', db.Integer, db.ForeignKey('equipment.id'), primary_key=True)
#                 ,db.Column('usage', db.Float, db.ForeignKey('equipment.current_usage'))
#                 # db.PrimaryKeyConstraint('clerk_id', 'equipment_id')
#                 )

class Transaction(db.Model):
    """
    Arguments
    ----------
        users
        clerks
        equipments
        usage

    Reference
    ----------
    .. [1] http://docs.sqlalchemy.org/en/latest/orm/extensions/associationproxy.html
    """
    __tablename__ = 'transaction'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    user_name = db.Column(db.Integer, db.ForeignKey('user.real_name', onupdate="CASCADE", ondelete="CASCADE"))

    clerk_id = db.Column(db.Integer, db.ForeignKey('clerk.id', onupdate="CASCADE", ondelete="CASCADE"))

    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id', onupdate="CASCADE", ondelete="CASCADE"))

    usage = db.Column(db.Float, db.ForeignKey('equipment.current_usage', onupdate="CASCADE", ondelete="CASCADE"))

    clerk = db.relationship('Clerk', backref=db.backref('transaction', uselist=False), foreign_keys=[clerk_id])
    user = db.relationship('User', backref=db.backref('transaction'), foreign_keys=[user_name])
    equipment = db.relationship('Equipment', backref=db.backref('transaction', uselist=False),foreign_keys=[equipment_id])
    company_bill = db.relationship("CompanyBill", backref="transaction")

    date = db.Column(db.DATETIME, default = datetime.utcnow())

    def __init__(self, **args):
        
        if (len(args) > 10):
            print("wrong args number")
            return
        self.__dict__.update(args)
        self.date = datetime.utcnow()

    @classmethod
    def get_transactions(self):
        transactions = db.session.query(Transaction).all()
        return transactions

    @classmethod
    def get_transactions_by_expression(self, expression):
        """
        expression: str
        """
        transactions = db.session.query(Transaction).filter(eval(expression))
        return transactions
    
    
    @classmethod
    def get_transaction_by_id(self, transaction_id):
        transaction = db.session.query(Transaction).filter(Transaction.id == transaction_id).first()
        return transaction


    @classmethod
    def get_transaction_by_expression(self, expression):
        """
        expression: str
        """
        transaction = db.session.query(Transaction).filter(eval(expression)).first()
        return transaction

    