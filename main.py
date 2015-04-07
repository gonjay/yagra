#! /usr/bin/python
#! -*- coding:utf-8 -*-

import os
import cgi
import Cookie
import yagra.lib as lib

print "Content-Type: text/html\n"
print os.environ
print lib.db_config

get "/" to mainpage.index
get "/sign_in" to Session.new
post "sign_in" to Session.create