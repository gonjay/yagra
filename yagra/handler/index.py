#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler
from ..lib.user import User

class MainHandler(BaseHandler):
    """docstring for MainHandler"""
    def get(self):
        user = self.current_user()
        if user is None:
            self.redirect_to("/sign_in")
        else:
            self.render_tplates(
                "users/profile.html",
                email=user.email,
                avatar_src=user.get_avatar())
