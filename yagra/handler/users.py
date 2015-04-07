#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

class UserHandler(BaseHandler):
    """A handler to create new user, manage upload avatar"""
    def __init__(self, arg):
        super(UserHandler, self).__init__()
        self.arg = arg
        