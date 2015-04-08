#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib
import sys

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
        self.headers = {}

    def set_header(self, k, v):
        self.headers[k] = v

    def gen_header_reponse(self):
        """Generate header response"""
        header_reponse = ["Status: %d %s" % (
            self.status_code,
            httplib.responses.get(self.status_code))]
        for k, v in self.headers.iteritems():
            header_reponse.append("%s: %s" % (k, v))
        return "\n".join(header_reponse) + "\r\n\r\n"

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

    def render(self, file, status_code=200, **kwargs):
        self.status_code = status_code
        sys.stdout.write(self.gen_header_reponse())
        sys.stdout.write(file)

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

