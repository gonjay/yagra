#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from yagra.handler.base import ErrorHandler

class App(object):
    """docstring for App"""
    def __init__(self):
        super(App, self).__init__()
        env = os.environ
        self.TEMPLATES_DIR = "yagra/templates"
        self.uri = env.get("REQUEST_URI")
        self.method = env.get("REQUEST_METHOD")

    def add_handlers(self, handlers):
        self.handlers = handlers

    def run(self):
        handler = None
        for (k, v) in self.handlers:
            if k == self.uri:
                handler = v(self)
                break
        if handler is None:
            handler = ErrorHandler(self)

        handler.execute(self.method)