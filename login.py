import sys
import web
import hashlib
import re
import base64
import sqlite3
from sqlite3 import *

web.config.debug = False
urls=('/','home','/results','login')

app = web.application(urls, globals(), True)

render = web.template.render('templates/')
store = web.session.DiskStore('sessions')
session = web.session.Session(app,store,initializer={'login': 0,'privilege': 0})
class home:
	def GET(self):
		return render.test()

	def POST(self):
		i = web.input()
		authdb = sqlite3.connect('users.db')
		conn = authdb.cursor()
#		pwdhash = hashlib.md5(i.password).hexdigest()
#		name=i.username;
		check = conn.execute('select * from user_names where username=? and password=?', (i.username, i.password))
	        n = conn.execute('select count(username) from user_names')
		print '.................',n
    		if check: 
			session.loggedin = True
        		session.username = i.username
        		raise web.seeother('/results')   
    		else: return render.test1('not logged in') 		


class login:
	def GET(self):
		return render.test1('logged in')

if __name__ == "__main__":
    app.run()

