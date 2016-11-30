# -*- coding=utf-8 -*-

from .. import db


class Clerk(db.Model):
    __tablename__ = 'clerk'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    equipment = db.relationship('Equipment', backref=db.backref('article'))

    def __init__(self, **args):
        if (len(args) > 5):
            print("wrong args number")
            return
        self.__dict__.update(args)
