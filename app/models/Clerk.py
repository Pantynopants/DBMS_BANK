# -*- coding=utf-8 -*-

from .. import db
# import Transaction

class Clerk(db.Model):
    __tablename__ = 'clerk'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # id_transaction = db.Column(db.Integer, db.ForeignKey("transaction.id"))
    # equipment = db.relationship('Equipment', backref=db.backref('clerk'))
    equipment_id = db.relationship(
        'Transaction' 
        # ,secondary = Transaction.Transaction
        ,backref=db.backref('clerks', lazy='joined')
        # ,primaryjoin = "Clerk.id==Transaction.transaction.c.clerk_id"
        # ,foreign_keys=[id]
        )

    def __init__(self, **args):
        if (len(args) > 5):
            print("wrong args number")
            return
        self.__dict__.update(args)

    @classmethod
    def get_clerks(self):
        clerks = db.session.query(Clerk).all()
        return clerks
    
    
    @classmethod
    def get_clerk_by_id(self, clerk_id):
        clerk = db.session.query(Clerk).filter(Clerk.id == clerk_id).first()
        return clerk

    @classmethod
    def get_clerk_by_expression(self, expression):
        """
        expression: str
        """
        clerk = db.session.query(Clerk).filter(eval(expression)).first()
        return clerk
