import os
import sys
import sha
import random
import string
import re
import hashlib
from lib import db_config as config

import MySQLdb as mdb
db = mdb.connect(
    config['host'],
    config['user'],
    config['password'],
    config['db'])
cur = db.cursor()

class User(object):
    """docstring for User"""
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.email = kwargs.get("email")
        self.password = kwargs.get("email")
        self.salt = kwargs.get("salt")
        self.token = kwargs.get("token")
        self.errors = []

    @staticmethod
    def query_user(sql):
        cur.execute(sql)
        row = cur.fetchone()
        if row is None:
            return None
        else:
            user = User(
                id=row[0], email=row[1],
                salt=row[2], token=row[3]
                )
            return user

    @staticmethod
    def insert_user(email, password):
        strs = string.ascii_uppercase + string.digits
        salt = ''.join(random.choice(strs) for _ in range(10))
        token = sha.new(salt + password).hexdigest()
        sql = "insert into user (email, salt, token) " \
        "values ('%s', '%s', '%s')" % (email, salt, token)
        cur.execute(sql)
        db.commit()
        return int(cur.lastrowid)

    @staticmethod
    def find_by_id(id):
        sql = "select * from user where id=%s limit 1" % id
        return User.query_user(sql)

    @staticmethod
    def find_by_email(email):
        sql = "select * from user where email='%s' limit 1" % email
        return User.query_user(sql)

    @staticmethod
    def create(**kwargs):
        user = User(**kwargs)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", user.email):
            user.errors.append("Email incorrect")
        if len(user.password) < 6:
            user.errors.append("Password too short")
        if User.find_by_email(user.email):
            user.errors.append("Email %s has been registered" % user.email)
        if len(user.errors) < 1:
            user.save()
        return user

    def update(self):
        strs = string.ascii_uppercase + string.digits
        salt = ''.join(random.choice(strs) for _ in range(10))
        token = sha.new(salt + self.password).hexdigest()
        sql = "update users set email = '%s', salt = '%s', token = '%s'" \
        "where id = %s" % (email, salt, token, id)
        cur.execute(sql)
        db.commit()
        return self

    def get_avatar(self):
        return hashlib.md5(self.email).hexdigest()

    def login(self, email, password):
        if User.find_by_email(email):
            token = sha.new(self.salt + password).hexdigest()
            if self.token != token:
                return None
            else:
                return self
        else:
            return None

    def save(self):
        if self.id is None or User.find_by_id(self.id) is None:
            self.id = User.insert_user(self.email, self.password)
        else:
            return self.update()

    def save_avatar(self, fileitem):
        extension = os.path.splitext(fileitem.filename)[1]
        if extension not in ['.jpg', '.png']:
            return "Only .jpg and .png allowed"
        if fileitem.filename:
            fn = self.get_avatar()
            file_dir_path = os.path.join("../", "file")
            if not os.path.isdir(file_dir_path):
                os.makedirs(file_dir_path)
            open(file_dir_path + "/" + fn, 'wb').write(fileitem.file.read())
            return "Your avatar was uploaded successfully"
        else:
            return "No file was uploaded"
