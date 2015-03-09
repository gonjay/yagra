#!/Users/GonJay/tmp/env/bin/python

import sha, time, Cookie, os, cgi
import cgitb; cgitb.enable()
from user import User

cookie = Cookie.SimpleCookie()
string_cookie = os.environ.get('HTTP_COOKIE')


def get_secret(uid):
    return sha.new("df29df0cb8df7c38143cb9344ba86510a5213bdc" + str(uid)).hexdigest()


def sign_in():
    print "Status: 303 See other"
    print "Location: /cgi-bin/sign_in.py"
    print # to end the CGI response headers.

if not string_cookie:
    sign_in()
else:
    cookie.load(string_cookie)
    secret = cookie.get('secret').value
    uid = cookie.get('uid').value
    if secret != get_secret(uid):
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
    <input class="form-control" type="file" value="" name="avatar"></div>

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
    if not form.has_key('avatar'):
        message = 'No file was selected'
    else:
        fileitem = form['avatar']
        if fileitem.filename:
            fn = user.get_avatar()
            file_dir_path = os.path.join("./", "file")
            if not os.path.isdir(file_dir_path):
                os.makedirs(file_dir_path)
            open(file_dir_path + "/" + fn, 'wb').write(fileitem.file.read())
            message = 'Your avatar was uploaded successfully'
        else:
            message = 'No file was uploaded'

    html = """\
    <html><body>
    <h1>%s</h1>
    <a href="/cgi-bin/yagra.py">Back</a>
    </body></html>
    """ % (message)

print "Content-Type: text/html\n"
print html