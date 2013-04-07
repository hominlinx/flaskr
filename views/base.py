#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, render_template

bp_base = Blueprint('base', __name__)

@bp_base.route('/base/')
def base():
    return 'blue print test'

@bp_base.route('/')
def index():

    url_map = {



            }

    return render_template('index.html', url_map=url_map)
