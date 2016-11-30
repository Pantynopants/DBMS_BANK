# -*- coding=utf-8 -*-

from .. import db
from datetime import datetime

class CompanyBill(db.Model):
    # __tablename__ = 'article'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), unique=True)
    body = db.Column(db.Text) # substract of this article
    create_time = db.Column(db.DATETIME, default = datetime.utcnow())

    def __init__(self, **args):
        
        if (len(args) > 5):
            print("wrong args number")
            return
        self.__dict__.update(args)