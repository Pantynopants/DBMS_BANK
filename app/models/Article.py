# # -*- coding=utf-8 -*-

# from .. import db, login_manager
# from datetime import datetime
# from werkzeug.security import generate_password_hash, check_password_hash 
# from flask_login import UserMixin 
# import hashlib

# class Article(db.Model):
#     # __tablename__ = 'article'
#     __table_args__ = {'extend_existing': True}
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(64), unique=True)
#     body = db.Column(db.Text) # substract of this article
#     create_time = db.Column(db.DATETIME, default = datetime.utcnow())
#     # category = db.relationship('Category', secondary=tags, backref=db.backref('articles'))
#     # user = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __init__(self, **args):
        
#         if (len(args) > 5):
#             print("wrong args number")
#             return
#         self.__dict__.update(args)