# -*- coding=utf-8 -*-

from .. import db

class BankAccount(db.Model):
    __tablename__ = 'bank_account'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_bank_bill = db.Column(db.Integer, db.ForeignKey('bank_bill.id', onupdate="CASCADE", ondelete="CASCADE"))

    total_money = db.Column(db.Float)

    def __init__(self, **args):
        
        if (len(args) > 5):
            print("wrong args number")
            return
        self.__dict__.update(args)

    @classmethod
    def get_bank_accounts(self):
        bank_accounts = db.session.query(BankAccount).all()
        return bank_accounts
    
    
    @classmethod
    def get_bank_account_by_id(self, bank_account_id):
        bank_account = db.session.query(BankAccount).filter(BankAccount.id == bank_account_id).first()
        return bank_account

    @classmethod
    def get_bank_account_by_expression(self, expression):
        """
        expression: str
        """
        bank_account = db.session.query(BankAccount).filter(eval(expression)).first()
        return bank_account


"""
db.backref('items', lazy='dynamic')
can only be used in many to many relationships
"""