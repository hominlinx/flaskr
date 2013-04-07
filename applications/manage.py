#!/usr/bin/env python
# encoding: utf-8


from flask import Flask

from flaskr.configs import settings
from flaskr.views.base import bp_base


def create_app(debug=settings.DEBUG):
    app = Flask(__name__)

    #是否debug模式
    app.debug = debug

    #注册蓝图
    app.register_blueprint(bp_base)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host=settings.SERVER_IP, port=settings.SERVER_PORT)
