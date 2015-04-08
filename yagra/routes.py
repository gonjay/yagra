#!/usr/bin/env python
# -*- coding: utf-8 -*-

import handler.index
import handler.sessions
import handler.users

handlers = [
    (r"/", handler.index.MainHandler),

    (r"/sign_in", handler.sessions.SessionHandler),
    (r"/logout", handler.sessions.SessionHandler),
    (r"/sign_up", handler.users.UserHandler),
    (r"/user/avatar", handler.users.UserHandler),
]
