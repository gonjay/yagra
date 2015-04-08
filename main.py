#! /usr/bin/python
#! -*- coding:utf-8 -*-

from yagra.application.app import App
from yagra import routes

def start():
    app = App()
    app.add_handlers(routes.handlers)
    app.run()


if __name__ == '__main__':
    start()