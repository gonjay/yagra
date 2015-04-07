#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

class SessionHandler(BaseHandler):
    """A Handler about session controll"""
    def __init__(self, arg):
        super(SessionHandler, self).__init__()
        self.arg = arg
        