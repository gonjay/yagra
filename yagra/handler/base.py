#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import sha, shelve, time, Cookie
import httplib
from ..lib.user import User

class HTTPError(Exception):
    """docstring for HTTPError"""
    def __init__(self, status_code):
        super(HTTPError, self).__init__()
        self.status_code = status_code

    def __str__(self):
        return "HTTP %d: %s" %\
            (self.status_code,
            httplib.responses.get(self.status_code))


class BaseHandler(object):
    """Base Handler to deal with CGI request"""
    def __init__(self, app):
        super(BaseHandler, self).__init__()
        self.app = app
        self.headers = {"Content-Type": "text/html"}
        self.session = Session()

    def set_header(self, k, v):
        self.headers[k] = v

    def gen_header_reponse(self):
        """Generate header response"""
        header_reponse = ["Status: %d %s" % (
            self.status_code,
            httplib.responses.get(self.status_code))]
        for k, v in self.headers.iteritems():
            header_reponse.append("%s: %s" % (k, v))
        return "\n".join(header_reponse) + "\n"\
               + str(self.session.cookie) + "\r\n\r\n"

    def current_user(self):
        uid = self.session.data.get("uid")
        return User.find_by_id(uid)

    def login_user(self, user):
        self.session.data["uid"] = user.id

    def send_error(self, status_code=405):
        self.render("<h1>Oooops</h1>",
            status_code=status_code)
        raise HTTPError(status_code)

    def redirect_to(self, path):
        self.set_header("Location", path)
        self.render("", status_code=303)

    def get(self):
        self.send_error()

    def post(self):
        self.send_error()

    def update(self):
        self.send_error()

    def delete(self):
        self.send_error()

    def render(self, content, status_code=200, **kwargs):
        self.session.close()
        self.status_code = status_code
        sys.stdout.write(self.gen_header_reponse())
        sys.stdout.write(content)

    def render_tplates(self, filename, **kwargs):
        filepath = os.path.join(self.app.TEMPLATES_DIR, filename)
        with open(filepath, 'r') as myfile:
            content = myfile.read()
        self.render(content % kwargs)

    def execute(self, method):
        if method.lower() == "get":
            self.get()
        elif method.lower() == "post":
            self.post()
        elif method.lower() == "update":
            self.update()
        elif method.lower() == "delete":
            self.delete()
        else:
            self.send_error()

class ErrorHandler(BaseHandler):
    """docstring for ErrorHandler"""

    def execute(self, method):
        self.send_error(status_code=404)

class Session(object):
    """docstring for Session"""
    def __init__(self):
        string_cookie = os.environ.get("HTTP_COOKIE", "")
        self.cookie = Cookie.SimpleCookie()
        self.cookie.load(string_cookie)

        if self.cookie.get("sid"):
            sid = self.cookie["sid"].value
        else:
            sid = sha.new(repr(time.time())).hexdigest()
        
        self.cookie.clear()

        self.cookie["sid"] = sid

        session_dir = "/tmp/session"

        if not os.path.exists(session_dir):
            try:
                os.mkdir(session_dir)
            except OSError, e:
                errmsg =  """%s when trying to create the session directory. \
                Create it as '%s'""" % (e, os.path.abspath(session_dir))
            raise OSError, errmsg

        sessid_dir = session_dir + "/sess_" + sid
        self.data = shelve.open(sessid_dir, writeback=True)

        if not self.data.get('cookie'):
            self.data['cookie'] = {'expires':''}

        self.set_expires(365*24*60*60)

    def close(self):
        self.data.close()

    def set_expires(self, expires=None):
        if expires == '':
            self.data['cookie']['expires'] = ''
        elif isinstance(expires, int):
            self.data['cookie']['expires'] = expires
        
        self.cookie['sid']['expires'] = self.data['cookie']['expires']

