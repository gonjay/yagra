#!/usr/bin/env python
# -*- coding: utf-8 -*-

class BaseHandler(object):
    """Base Handler to deal with CGI request"""
    def __init__(self, arg):
        super(BaseHandler, self).__init__()
        self.arg = arg
        