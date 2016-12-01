# -*- coding=utf-8 -*-
from models import *
def init_DB_data(db):

    
    
    # a1 = Article.Article(title = "a1", body = 'a1a1a1a1a1a1a1a1a1a1a1a1a1a1a1')
    # a2 = Article.Article(title = "a2", body = "a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2")
    # a3 = Article.Article(title = "a3", body = "a3a3a3a3a3a3a3a3a3a3a3a3a3a3a3")
    # a4 = Article.Article(title = "a4", body = "a4a4a4a4a4a4a4a4a4a4a4a4a4a4a4")

    # c1 = Category(name = "c1")
    # c2 = Category(name = "c2")
    c1 = Clerk.Clerk()
    e1 = Equipment.Equipment()
    e2 = Equipment.Equipment()
    e1.current_usage = 1
    e2.current_usage = 2
    u1 = User.User(username = "u1u1u1",  real_name = "u1 u1")
    u2 = User.User(username = "u2u2u2",  real_name = "u2 u2")

    # c1.equipments = [e1, e2]
    t1 = Transaction.Transaction()
    t1.users = u1
    t1.user_name = u1.real_name
    t1.equipments = e1
    t1.clerks = c1
    t1.usage = 10
    # u1.article = [e1, e2]
    # u2.article = [a3, a4]

    # c1.article = [a1, a2, a4]
    # c2.article = [a2, a3]

    #a1...a4.category    
    
    from utils.db_utils import commit_data
    commit_data(db, c1, e1, e2, u1,u2, t1)
    # print(u1.password_hash)
    from test.db_test import DB_test
    DB_test(db)

    return db