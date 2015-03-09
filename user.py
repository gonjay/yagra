#!/Users/GonJay/tmp/env/bin/python

import os
import sys
import sha
import random
import string
import re
import hashlib
from lib import db_config as config


class User():
    """docstring for User"""
    def __init__(self):
        import MySQLdb as mdb
        self.db = mdb.connect(
            config['host'],
            config['user'],
            config['password'],
            config['db'])
        self.cur = self.db.cursor()

    def query(self, sql):
        self.cur.execute(sql)
        row = self.cur.fetchone()
        if row is None:
            return None
        else:
            self.id = row[0]
            self.email = row[1]
            self.salt = row[2]
            self.token = row[3]
            return self

    def find_by_id(self, id):
        sql = "select * from user where id=%s limit 1" % id
        return self.query(sql)

    def find_by_email(self, email):
        sql = "select * from user where email='%s' limit 1" % email
        return self.query(sql)

    def get_avatar(self):
        return hashlib.md5(self.email).hexdigest()

    def login(self, email, password):
        if self.find_by_email(email):
            token = sha.new(self.salt + password).hexdigest()
            if self.token != token:
                return None
            else:
                return self
        else:
            return None

    def create(self, email, password):
        if len(password) < 6:
            return "Password too short"
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Email incorrect"
        elif self.find_by_email(email):
            return "Email %s has been registered" % email
        else:
            strs = string.ascii_uppercase + string.digits
            salt = ''.join(random.choice(strs) for _ in range(10))
            token = sha.new(salt + password).hexdigest()
            sql = "insert into user (email, salt, token) " \
                  "values ('%s', '%s', '%s')" % (email, salt, token)
            self.cur.execute(sql)
            self.db.commit()
            self.id = self.cur.lastrowid
            return True

    def save_avatar(self, fileitem):
        if fileitem.filename:
            fn = self.get_avatar()
            file_dir_path = os.path.join("./", "file")
            if not os.path.isdir(file_dir_path):
                os.makedirs(file_dir_path)
            open(file_dir_path + "/" + fn, 'wb').write(fileitem.file.read())
            return 'Your avatar was uploaded successfully'
        else:
            return 'No file was uploaded'
