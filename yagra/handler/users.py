#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

class UserHandler(BaseHandler):

    def get(self):
        self.render_tplates("users/new.html")