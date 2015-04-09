#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler
from ..lib.user import User

class MainHandler(BaseHandler):
    """docstring for MainHandler"""
    def get(self):
        """Get a home page"""
        user = self.current_user()
        if user is None:
            self.redirect_to("/sign_in")
        else:
            self.render_tplates(
                "users/profile.html",
                email=user.email,
                avatar_src=user.get_avatar())

    def post(self):
        user = self.current_user()
        if 'avatar' not in self.form:
            message = 'No file was selected'
        else:
            fileitem = self.form['avatar']
            message = user.save_avatar(fileitem)
        html = """\
        <html><body>
        <h1>%s</h1>
        <a href="/">Back</a>
        </body></html>
        """ % (message)
        self.render(html)
