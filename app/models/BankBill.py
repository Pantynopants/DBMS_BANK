# -*- coding=utf-8 -*-
from datetime import datetime
import random
from .. import db

class BankBill(db.Model):
    __tablename__ = 'bank_bill'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    

    date = db.Column(db.DATETIME, default = datetime.utcnow())
    total_exchange = db.Column(db.Float)
    transaction_number = db.Column(db.Integer)

    def __init__(self, **args):
        
        if (len(args) > 4):
            print("wrong args number")
            return
        self.__dict__.update(args)

class BankBillItem(db.Model):
    __tablename__ = 'bank_bill_item'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    id_bank_bill = db.Column(db.Integer, db.ForeignKey('bank_bill.id'))
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    serial_number = db.Column(db.Integer, default = random.randint(1000, 9999))

    date = db.Column(db.DATETIME, db.ForeignKey('bank_bill.date'))
    exchange = db.Column(db.Float)

    def __init__(self, **args):
        
        if (len(args) > 5):
            print("wrong args number")
            return
        self.__dict__.update(args)