# -*- coding=utf-8 -*-
from models import *
def init_DB_data(db):

    
    c1 = Clerk.Clerk()
    c2 = Clerk.Clerk()
    e1 = Equipment.Equipment()
    e2 = Equipment.Equipment()
    e3 = Equipment.Equipment()
    # TODO
    e1.current_usage = 1
    e2.current_usage = 2
    
    u1 = User.User()
    u1.username = "u1u1u1" 
    u1.real_name = "u1 u1"
    u1.password = "aaaaaa"

    u2 = User.User()
    u2.username = "20144695" 
    u2.real_name = "20144695"
    u2.password = "aaaaaa"

    # u2 = User.User(username = "u2u2u2",  real_name = "u2 u2")
    
    # c1.equipments = [e1, e2]
    t1 = Clerk.Clerk.check_usage_to_trans(user = u1, clerks = c1, equipments = e1, usage = 10)

    t2 = Clerk.Clerk.check_usage_to_trans(user = u1, clerks = c2, equipments = e2, usage = 15)
    
    t3 = Clerk.Clerk.check_usage_to_trans(user = u2, clerks = c1, equipments = e3, usage = 22)
    # u1.article = [e1, e2]
    # u1.transaction = t1

    #a1...a4.category    
    
    from utils.db_utils import commit_data
    commit_data(db, c1, e1, e2, u1,u2, t1, t2, t3)
    print(u2.username)

    

    from test.db_test import DB_test
    DB_test(db)

    return db