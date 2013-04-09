#!/usr/bin/env python
# encoding: utf-8


from flask import Flask, url_for

from flaskr.configs import settings
from flaskr.views.base import bp_base


def create_app(debug=settings.DEBUG):
    app = Flask(__name__,
                template_folder=settings.TEMPLATE_FOLDER,
                static_folder=settings.STATIC_FOLDER)

    app.logger.debug('hello world, from log')
    #是否debug模式
    app.debug = debug

    #注册蓝图
    app.register_blueprint(bp_base)

    #for session
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

    return app

app = create_app()

if __name__ == '__main__':

    #TODO: not right
    #############
    #  url for#
    #############
    #with app.test_request_context():
    #    print url_for('bp_base')

    #app.run(host='0.0.0.0') 确保外部课件，使用对外开放的ip
    app.run(host=settings.SERVER_IP, port=settings.SERVER_PORT)


