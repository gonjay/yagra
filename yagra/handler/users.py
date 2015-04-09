#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler
from ..lib.user import User

class UserHandler(BaseHandler):

    def get(self):
        """Get sign up page"""
        self.render_tplates("users/new.html")

    def post(self):
        """Create a new user"""
        email = self.form.getvalue('email', '')
        password = self.form.getvalue('password', '')
        password_confirm = self.form.getvalue('password_confirm', '')
        user = User.create(
            email=email,
            password=password,
            password_confirm=password_confirm)
        if len(user.errors) < 1:
            self.login_user(user)
            self.redirect_to("/")
        else:
            html = """
            <html><body>
            <h1>Errors</h1>
            <p>%s</p>
            <a href="/sign_up">Back</a>
            </body></html>
            """ % "<br><br>".join(user.errors)
            self.render(html)

    def update(self):
        """Update user avatar"""
        self.redirect_to("/")