#!/Users/GonJay/tmp/env/bin/python

import sha

# Replae secret_token when deploy
secret_token = "df29df0cb8df7c38143cb9344ba86510a5213bdc"

db_config = {
    'host': 'localhost',
    'user': 'yagra',
    'password': '123456',
    'db': 'yagra'
}


def get_secret(uid):
    return sha.new(str(uid)).hexdigest()
