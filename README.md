# DB_BANK
A demo of flask-sqlalchemy, flask-bootstrap, Flask-Script and flask-wtf, with DB practice


>  experiment of college's DB experiment, 2016.12

---

## Using 

### environment   
1. clone it  
2. `python install -r requirements.txt`  

*Flask-Script* as command tool   
### first time run you should do:  

`python manage.py db init`  

### after change the DB model u should do:  

`python manage.py db migrate -m "first init db"`  
`python manage.py db upgrade`  
*or *  `python _dev.py` * to delete them and init again*  

### always run:  
`python manage.py runserver`

## structure 
`/app` for MVC files  
`/config.py` for DB connect and SQLALCHEMY options   
`/manage.py` for `@app.before_request`  
...  


## libs 
- [flask-sqlalchemy](http://flask-sqlalchemy.pocoo.org/2.1/api/)
- flask-bootstrap
- flask-wtf
- [sqlchemy](docs.sqlalchemy.org/en/latest/index.html)
- [werkzeug](http://werkzeug.pocoo.org/docs/0.11/utils/)  
- oracle
- [mysql.procedure](https://github.com/Pantynopants/DBMS_BANK/blob/master/sql/procedure.sql)
- sqlite

---  

    
## ref
- jinja2:  
http://flask.pocoo.org/docs/0.11/tutorial/templates/  
http://flask.pocoo.org/docs/0.11/quickstart/#rendering-templates  
https://pythonhosted.org/Flask-Bootstrap/basic-usage.html  
http://wtforms.simplecodes.com/docs/0.6.1/validators.html  
https://code-maven.com/using-templates-in-flask  
http://docs.jinkan.org/docs/jinja2/templates.html#template-inheritance  
http://www.oschina.net/question/5189_3943  
- cookie:  
https://www.douban.com/group/topic/12750952/  
- Blueprint:  
http://www.cnblogs.com/ymy124/p/4417525.html  

https://github.com/mjhea0/flask-boilerplate
---


## screenshots 
![db_refund](https://github.com/Pantynopants/DBMS_BANK/blob/master/11.PNG)

![db_transactions](https://github.com/Pantynopants/DBMS_BANK/blob/master/9.PNG)


btw, welcome issue n star ;)
