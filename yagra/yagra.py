#!/usr/bin/env python

import os
import cgi
import Cookie
import cgitb
import lib
from user import User

cgitb.enable()

cookie = Cookie.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')


def sign_in():
    print "Status: 303 See other"
    print "Location: /cgi-bin/sign_in.py"
    print

if not string_cookie:
    sign_in()
else:
    cookie.load(string_cookie)
    secret = cookie.get('secret').value
    uid = cookie.get('uid').value
    if secret != lib.get_secret(uid):
        sign_in()

user = User()
user.find_by_id(uid)

if os.environ['REQUEST_METHOD'] == 'GET':
    html = """\
    <html>
    <head><link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.2/css/bootstrap.min.css"></head>
    <body>
    <div class="container">
    <div class="row">
    <div class="col-md-4">
    <h1>Yagra</h1>
    <h3>Welcome, %s</h3>
    <img src="/avatar/%s" onerror="javascript:this.src='/avatar/default.png'";>
    <br><br>

    <form enctype="multipart/form-data" action="/cgi-bin/yagra.py" accept-charset="UTF-8" method="post">
    <div class="form-group"><label for="user_avatar">Upload Avatar</label><br>
    <input class="form-control" type="file" value="" name="avatar" accept="image/*"></div>

    <div class="form-group">
    <input type="submit" name="commit" value="Submit" class="btn btn-primary">
    </div>
    </form>

    <a href="/cgi-bin/sign_in.py" class="btn">Sign out</a><br>

    </div>
    </div>
    </div>
    </body></html>
    """ % (user.email, user.get_avatar())
elif os.environ['REQUEST_METHOD'] == 'POST':
    form = cgi.FieldStorage()
    if 'avatar' not in form:
        message = 'No file was selected'
    else:
        fileitem = form['avatar']
        message = user.save_avatar(fileitem)

    html = """\
    <html><body>
    <h1>%s</h1>
    <a href="/cgi-bin/yagra.py">Back</a>
    </body></html>
    """ % (message)

print "Content-Type: text/html\n"
print html
