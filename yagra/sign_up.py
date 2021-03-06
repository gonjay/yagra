#!/usr/bin/env python

import os
import cgi
import Cookie
import lib
from user import User

if os.environ['REQUEST_METHOD'] == 'GET':
    html = """\
    <html>
    <head><link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.2/css/bootstrap.min.css"></head>
    <body>
    <div class="container">
    <div class="row">
    <div class="col-md-4">
    <h2>Sign up</h2>

    <form class="new_user" id="new_user" action="/cgi-bin/sign_up.py" accept-charset="UTF-8" method="post">

    <div class="form-group"><label for="user_email">Email</label><br>
    <input autofocus="autofocus" class="form-control" type="email" value="" name="email" id="user_email"></div>

    <div class="form-group"><label for="user_password">Password</label><br>
    <input class="form-control" type="password" name="password" id="user_password"></div>

    <div class="form-group"><label for="user_confirm_password">Confirm password</label><br>
    <input class="form-control" type="password" name="password_confirm" id="user_password_confirmation"></div>

    <div class="form-group">
    <input type="submit" name="commit" value="Sign up" class="btn btn-primary">
    </div>
    </form>
    <a href="/cgi-bin/sign_in.py">Sign in</a><br>

    </div>
    </div>
    </div>
    </body></html>
    """
elif os.environ['REQUEST_METHOD'] == 'POST':
    form = cgi.FieldStorage()
    email = form.getvalue('email', '')
    password = form.getvalue('password', '')
    password_confirm = form.getvalue('password_confirm', '')
    user = User()
    result = user.create(email, password, password_confirm)

    if result is True:
        cookie = Cookie.SimpleCookie()
        secret = lib.get_secret(user.id)
        cookie['secret'] = secret
        cookie['uid'] = user.id
        print cookie
        print "Status: 303 See other"
        print "Location: /cgi-bin/yagra.py"
        print

    html = """\
    <html><body>
    <h1>Something wrong</h1>
    <p>%s</p>
    <a href="/cgi-bin/sign_up.py">Back</a>
    </body></html>
    """ % result

print "Content-Type: text/html\n"
print html
