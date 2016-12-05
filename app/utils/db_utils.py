# -*- coding=utf-8 -*-

from flask import Flask, request, make_response
import hashlib
import functools

SALT = "@#3k25l23#KW#LRsekr@#"

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


