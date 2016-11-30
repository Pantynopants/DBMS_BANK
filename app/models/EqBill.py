# -*- coding=utf-8 -*-

from .. import db
from datetime import datetime

class EqBill(db.Model):
    __tablename__ = 'eq_bill'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    id_clerk = db.Column(db.Integer, db.ForeignKey('clerk.id'))
    id_equipment = db.Column(db.Integer, db.ForeignKey('equipment.id'))

    current_usage = db.Column(db.Float, db.ForeignKey('equipment.current_usage'))
    date = db.Column(db.DATETIME, default = datetime.utcnow())


    def __init__(self, **args):
        
        if (len(args) > 4):
            print("wrong args number")
            return
        self.__dict__.update(args)