# -*- coding=utf-8 -*-
from ..utils.db_utils import *
from ..models import *
def DB_test(db):

    print(Equipment.Equipment.get_equipment_by_id(1).current_usage)
    print(Equipment.Equipment.query.get(1).current_usage)
    print type(Clerk.Clerk.query.all())
    print(Transaction.Transaction.query.get(1).usage)
    u1 = User.User.query.get(1)
    print("#"*40)
    for i in u1.get_my_trans():
        print(i.usage)

    print("TEST get_user_by_username()")
    u_ = User.User.get_user_by_username('u1u1u1')
    print(u_.real_name)

    u1.pay_trans(trans = [], number = 15)
    commit_data(db, u1)
    print("#"*40)
    print("BankBillItem")
    # for i in BankBill.BankBillItem.query.all():
    #     print (i.get_user_name())
    print("#"*40)
    for i in u1.get_my_trans():
        print(i.usage)
    print("#"*40)
    for i in Transaction.Transaction.query.all():
        print(i.usage)
    print("#"*40)
    for i in User.User.query.get(1).get_bank_bill_items():
        print(i.serial_number)
    print("#"*40)
    for i in CompanyBill.CompanyBill.query.all():
        print(i.date)
    print("#"*40)
    # print db.session.query(Transaction.Transaction).filter(Transaction.Transaction.user_name == "u1 u1").first()

    # u1 = User.User.query.get(1)
    # s_number = u1.get_bank_bill_items()[0].serial_number
    # print(s_number)
    # u1.refund_trans(serial_number=s_number, number=10)
    # print("#"*40)
    # for i in Transaction.Transaction.query.all():
    #     print(i.usage)
    # print("#"*40)
    print(BankBill.BankBillItem.get_today_info())
    print User.User.get_my_bank_bill_items(u1.real_name)[0].serial_number
    print BankBill.BankBillItem.get_bank_bill_by_serial_num(User.User.get_my_bank_bill_items(u1.real_name)[0].serial_number).get_today_info()
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

    # clear_test(db)
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