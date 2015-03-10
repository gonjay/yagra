#!/Users/GonJay/tmp/env/bin/python

import os
import cgi
import Cookie
import lib
from user import User
cookie = Cookie.SimpleCookie()

cookie['secret'] = ''
cookie['uid'] = ''

if os.environ['REQUEST_METHOD'] == 'GET':
    html = """\
    <html>
    <head><link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.2/css/bootstrap.min.css"></head>
    <body>
    <div class="container">
    <div class="row">
    <div class="col-md-4">
    <h2>Sign in</h2>

    <form class="new_user" id="new_user" action="/cgi-bin/sign_in.py" accept-charset="UTF-8" method="post">
    <div class="form-group"><label for="user_email">Email</label><br>
    <input autofocus="autofocus" class="form-control" type="email" value="" name="email" id="user_email"></div>

    <div class="form-group"><label for="user_password">Password</label><br>
    <input class="form-control" type="password" name="password" id="user_password"></div>

    <div class="form-group">
    <input type="submit" name="commit" value="Sign in" class="btn btn-primary">
    </div>
    </form>

    <a href="/cgi-bin/sign_up.py">Sign up</a><br>

    </div>
    </div>
    </div>
    </body></html>
    """
elif os.environ['REQUEST_METHOD'] == 'POST':
    form = cgi.FieldStorage()
    email = form.getvalue('email', '')
    password = form.getvalue('password', '')
    user = User()
    result = user.login(email, password)

    if result is not None:
        cookie['secret'] = lib.get_secret(user.id)
        cookie['uid'] = user.id
        print cookie
        print "Status: 303 See other"
        print "Location: /cgi-bin/yagra.py"
        print

    html = """\
    <html><body>
    <h1>Password or Email incorrect</h1>
    <a href="/cgi-bin/sign_in.py">Back</a>
    </body></html>
    """

print cookie
print "Content-Type: text/html\n"
print html
