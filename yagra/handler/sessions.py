#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import BaseHandler

class SessionHandler(BaseHandler):

    def get(self):
        self.render_tplates("sessions/new.html")