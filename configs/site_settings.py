#!/usr/bin/env python
# encoding: utf-8
import os

DEBUG = True


SERVER_IP = '127.0.0.1'
SERVER_PORT = 8088


PROJECT_DIR =  os.path.dirname(__file__)
TEMPLATE_FOLDER = os.path.join(PROJECT_DIR, '../templates')
STATIC_FOLDER = os.path.join(PROJECT_DIR, '../media')
