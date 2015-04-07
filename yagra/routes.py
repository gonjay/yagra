#!/usr/bin/env python
# -*- coding: utf-8 -*-

import handler.index
import handler.session
import handler.user

handlers = [
    (r"/", handler.index.MainHandler),

    (r"/sign_in", handler.session.SessionHandler),
    (r"/logout", handler.session.SessionHandler),
    (r"/sign_up", handler.user.UserHandler),
    (r"/user/avatar", handler.user.UserHandler),
]
