#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib

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

    def get(self):
        raise HTTPError(405)

    def post(self):
        raise HTTPError(405)

    def update(self):
        raise HTTPError(405)

    def delete(self):
        raise HTTPError(405)

    def execute(self, method):
        pass

class ErrorHandler(BaseHandler):
    """docstring for ErrorHandler"""
    def execute(self, method):
        raise HTTPError(404)