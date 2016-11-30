# -*- coding=utf-8 -*-
from ..utils.db_utils import *
from ..models import *
def DB_test(db):

    # print(type(Article.query.get(1).body))
    u = Article.Article.query.get(2).body
    tempu = u.encode('raw_unicode_escape')
    print(type(tempu), tempu, tempu == 'a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2')
    # print(Article.query.filter(Article.body == u'a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2').first())
    if Article.Article.query.filter(Article.Article.title == u'a2').count() > 0:
        print("success commit")
        # print(Article.query.filter(Article.body == u'a2a2a2a2a2a2a2a2a2a2a2a2a2a2a2').first().title)
    # print(Article.query.get(3).title)

    user = User.User.query.filter(User.User.username == "u1u1u1")
    if user.count() > 0:
        print("success commit")
        # print user.first().user_cookies

    clear_test(db)
    print("print None")
    print(Article.Article.query.all())

    return 