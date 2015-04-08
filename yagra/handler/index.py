#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

class MainHandler(BaseHandler):
    """docstring for MainHandler"""
    def get(self):
        self.redirect_to("/sign_in")
