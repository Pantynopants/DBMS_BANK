# -*- coding=utf-8 -*-
from datetime import datetime
import random
from .. import db
import User
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

    @classmethod
    def get_bank_bills(self):
        bank_bills = db.session.query(BankBill).all()
        return bank_bills
    
    
    @classmethod
    def get_bank_bill_by_id(self, bank_bill_id):
        bank_bill = db.session.query(BankBill).filter(BankBill.id == bank_bill_id).first()
        return bank_bill

    @classmethod
    def get_bank_bill_by_expression(self, expression):
        """
        expression: str
        """
        bank_bill = db.session.query(BankBill).filter(eval(expression)).first()
        return bank_bill

class BankBillItem(db.Model):
    __tablename__ = 'bank_bill_item'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    user_name = db.Column(db.Integer, db.ForeignKey('user.real_name', onupdate="CASCADE", ondelete="CASCADE"))
    id_user = db.relationship('User', backref=db.backref('bank_bill_item'), foreign_keys=[user_name])

    id_bank_bill = db.Column(db.Integer, db.ForeignKey('bank_bill.id'))

    bank = db.Column(db.Integer)

    serial_number = db.Column(db.Integer, default = random.randint(1000, 9999))

    date = db.Column(db.DATETIME, default = datetime.utcnow())
    exchange = db.Column(db.Float)

    # id_company_bill = db.Column(db.Integer, db.ForeignKey('company_bill.id'))
    company_bill = db.relationship('CompanyBill', backref=db.backref('bank_bill_item'))

    def __init__(self, **args):
        
        if (len(args) > 9):
            print("wrong args number")
            return
        self.__dict__.update(args)
        self.date = datetime.utcnow()

    @classmethod
    def get_bank_bill_items(self):
        bank_bill_items = db.session.query(BankBillItem).all()
        return bank_bill_items
    
    
    @classmethod
    def get_bank_bill_item_by_id(self, bank_bill_item_id):
        bank_bill_item = db.session.query(BankBillItem).filter(BankBillItem.id == bank_bill_item_id).first()
        return bank_bill_item

    @classmethod
    def get_bank_bill_item_by_expression(self, expression):
        """
        expression: str
        """
        bank_bill_item = db.session.query(BankBillItem).filter(eval(expression)).first()
        return bank_bill_item

    @classmethod
    def get_total_money_in_date(self):
        total_money = 0
        for i in db.session.query(BankBillItem).all():
            if i.exchange == None:
                continue
            total_money += i.exchange
        return total_money

    @classmethod
    def get_total_trans_number_in_date(self):
        return len(db.session.query(BankBillItem).all())

    @classmethod
    def get_date(self):
        try:
            time = str(db.session.query(BankBillItem).first().date)[5:10]
        except :
            print("None BankBillItem found! return 000000 as time") 
            time = str(000000)
        return time

    # @classmethod
    # def get_user_name(self):
    #     return db.session.query(User.User).filter(User.User.bank_bill_items.serial_number == self.serial_number).first()

    @staticmethod
    def get_today_info():
        # print("user\t", (BankBillItem.get_user_name()))
        print("money\t", BankBillItem.get_total_money_in_date())
        print("trans_number\t", BankBillItem.get_total_trans_number_in_date())
        print("date\t", (BankBillItem.get_date()))

    @staticmethod
    def get_bank_bill_by_serial_num(serial_num):
        """return a bankbill
        """
        return db.session.query(BankBillItem).filter(BankBillItem.serial_number == serial_num).first()