# -*- coding=utf-8 -*-

from .. import db

import Transaction

class Equipment(db.Model):
    __tablename__ = 'equipment'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # id_transaction = db.Column(db.Integer, db.ForeignKey("transaction.id"))
    clerk_id = db.relationship(
        'Transaction' 
        # ,secondary = Transaction.Transaction 
        ,backref=db.backref('equipments', lazy='joined')
        ,foreign_keys=[Transaction.Transaction.equipment_id]
        # ,primaryjoin = "Equipment.id==Transaction.transaction.c.equipment_id"
        # secondaryjoin = id==Transaction.transaction.c.right_node_id,
        )

    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    # id_eq_bill = db.relationship('EqBill', backref=db.backref('equipment'))

    current_usage = db.Column(db.Float)

    def __init__(self, **args):
        
        if (len(args) > 4):
            print("wrong args number")
            return
        self.__dict__.update(args)

    @classmethod
    def get_equipments(self):
        equipments = db.session.query(Equipment).all()
        return equipments
    
    
    @classmethod
    def get_equipment_by_id(self, equipment_id):
        equipment = db.session.query(Equipment).filter(Equipment.id == equipment_id).first()
        return equipment

    @classmethod
    def get_equipment_by_expression(self, expression):
        """
        expression: str
        """
        equipment = db.session.query(Equipment).filter(eval(expression)).first()
        return equipment



"""
http://docs.sqlalchemy.org/en/latest/orm/join_conditions.html

http://stackoverflow.com/questions/34234964/flask-and-sqlalchemy-noforeignkeyserror-could-not-determine-join-condition-betw
"""