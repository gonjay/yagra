#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler
from ..lib.user import User

class SessionHandler(BaseHandler):

    def get(self):
        """Get sign in page"""
        self.render_tplates("sessions/new.html")


    def post(self):
        """Post email and password to login"""
        email = self.form.getvalue('email', '')
        password = self.form.getvalue('password', '')
        user = User().auth(email, password)

        if user is not None:
            self.login_user(user)
            self.redirect_to("/")
        else:
            html = """\
            <html><body>
            <h1>Password or Email incorrect</h1>
            <a href="/sign_in">Back</a>
            </body></html>
            """
            self.render(html)

    def delete(self):
        pass