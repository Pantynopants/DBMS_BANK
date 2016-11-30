# -*- coding=utf-8 -*-

from .. import db

class BankAccount(db.Model):
    __tablename__ = 'bank_account'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_bank_bill = db.Column(db.Integer, db.ForeignKey('bank_bill.id'))

    total_money = db.Column(db.Float)

    def __init__(self, **args):
        
        if (len(args) > 5):
            print("wrong args number")
            return
        self.__dict__.update(args)