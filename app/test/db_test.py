# -*- coding=utf-8 -*-
from ..utils.db_utils import *
from ..models import *
def DB_test(db):

    print(Equipment.Equipment.get_equipment_by_id(1).current_usage)
    print(Equipment.Equipment.query.get(1).current_usage)
    print(Clerk.Clerk.query.all())
    print(Transaction.Transaction.query.get(1).user_name)
    # print db.session.query(Transaction.Transaction).filter(Transaction.Transaction.user_name == "u1 u1").first()
    print(User.User.get_trans_by_user_id("u1 u1").usage)


    # u = Article.Article.query.get(2).body
    # tempu = u.encode('raw_unicode_escape')
    # print(type(tempu), tempu, tempu == 'a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2')
    # # print(Article.query.filter(Article.body == u'a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2').first())
    # if Article.Article.query.filter(Article.Article.title == u'a2').count() > 0:
    #     print("success commit")
    #     # print(Article.query.filter(Article.body == u'a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2').first().title)
    # # print(Article.query.get(3).title)

    # user = User.User.query.filter(User.User.username == "u1u1u1")
    # if user.count() > 0:
    #     print("success commit")
    #     # print user.first().user_cookies

    clear_test(db)
    print("print None")
    # print(Article.Article.query.all())

    return 


"""
clerk
1. generate transaction(to company)

user
1. get transaction
2. pay transaction(company, bank)
3. refund (company, bank)

company
1. check total transaction (bank)
2. check individual transaction(bank)
"""