# -*- coding=utf-8 -*-

from .. import db

class Transaction(db.Model):
    __tablename__ = 'transaction'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))

    usage = db.Column(db.Float, db.ForeignKey('equipment.current_usage'))

    def __init__(self, **args):
        
        if (len(args) > 2):
            print("wrong args number")
            return
        self.__dict__.update(args)