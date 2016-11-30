# -*- coding=utf-8 -*-
from ..models import *
from flask import Flask, request, make_response
import hashlib

def clear_test(db):
    db.drop_all(bind=None)
    db.create_all()
    
def commit_data(db, *data):
    from sqlalchemy import exc

    try:
        db.session.add_all(data)
        db.session.commit()
    except exc.IntegrityError:
        db.session.rollback()
        print 'This item fails one of the unique/foreign key checks!'
    except:
        print 'There was another error'
        raise
    else:
        print 'Everything is OK'


def isUserAwesome( username):
    return username == "administrator"

def makeCookie( userid):
    user_cookies = "%s|%s" %(userid, hashlib.sha256(userid+SALT).hexdigest())
    return user_cookies

def isCookieValid( cookie):
    (userid, hashed) = parseCookie(cookie)
    return hashed == hashlib.sha256(userid+SALT).hexdigest()


def parseCookie( cookie):
    parsed = cookie.split("|")
    userid = parsed[0]
    if (len(parsed) > 1):
        hashed = parsed[1]
    else:
        hashed = ""
    return (userid, hashed)

def isUserExist(name):   
    """
    exist:return true
    """
    return User.query.filter(User.username == name).count() != 0


def vaildation_user(request):
    """
    para:
        request(Flask.request)
    return:
        True, user(Model.User)
        or
        False, None

    """
    cookie = request.cookies.get('USERID', 'GUEST')
    (userid, hashed) = parseCookie(cookie)
    user = User.query.filter(User.username == userid).first()
    # suc_message = "admin log in"
    # ordinary_message = "user log in"
    # norm_message = "guest log in"
    
    # if isUserAwesome(userid) and isCookieValid(cookie):
    #     resp = make_response(suc_message)
    #     resp.set_cookie("USERID", makeCookie("administrator"))
    if isUserExist(userid) and isCookieValid(cookie) and user is not None and userid != "GUEST":
        return True, user
        # resp = make_response(ordinary_message)
        # user = User.query.filter(User.username == name).first()

        # resp.set_cookie("USERID", user.user_cookies)
    else:
        return False, user
        # resp = make_response(norm_message)
        # resp.set_cookie("USERID", makeCookie("GUEST"))
    # return resp