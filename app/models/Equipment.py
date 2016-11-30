# -*- coding=utf-8 -*-

from .. import db

class Equipment(db.Model):
    __tablename__ = 'equipment'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    id_clerk = db.Column(db.Integer, db.ForeignKey('clerk.id'))

    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    id_eq_bill = db.Column(db.Integer, db.ForeignKey('eq_bill.id'))

    current_usage = db.Column(db.Float)

    def __init__(self, **args):
        
        if (len(args) > 3):
            print("wrong args number")
            return
        self.__dict__.update(args)