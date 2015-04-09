#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

class MainHandler(BaseHandler):
    """docstring for MainHandler"""
    def get(self):
        self.render_tplates(
            "users/profile.html",
            email="user.email",
            avatar_src="user.getAvatar()")
