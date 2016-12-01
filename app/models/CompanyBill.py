# -*- coding=utf-8 -*-

from .. import db
from datetime import datetime

class CompanyBill(db.Model):
    __tablename__ = 'company_bill'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_bank_bill = db.Column(db.Integer, db.ForeignKey('bank_bill.id', onupdate="CASCADE", ondelete="CASCADE"))
    date = db.Column(db.DATETIME, default = datetime.utcnow())
    money = db.Column(db.Float)

    def __init__(self, **args):
        
        if (len(args) > 5):
            print("wrong args number")
            return
        self.__dict__.update(args)

    @classmethod
    def get_company_bills(self):
        company_bills = db.session.query(CompanyBill).all()
        return company_bills
    
    
    @classmethod
    def get_company_bill_by_id(self, company_bill_id):
        company_bill = db.session.query(CompanyBill).filter(CompanyBill.id == company_bill_id).first()
        return company_bill

    @classmethod
    def get_company_bill_by_expression(self, expression):
        """
        expression: str
        """
        company_bill = db.session.query(CompanyBill).filter(eval(expression)).first()
        return company_bill