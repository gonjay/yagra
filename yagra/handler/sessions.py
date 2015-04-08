#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

class SessionHandler(BaseHandler):

    def get(self):
        self.render("<h1>hihi</h1>")