#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint, render_template, url_for, request

# for file upload
from werkzeug import secure_filename
# for cookie
from flask import make_response
# for redirect
from flask import redirect
# for session
from flask import session

bp_base = Blueprint('base', __name__)


@bp_base.route('/')
def index():
    url_map = {



            }

    return render_template('index.html', url_map=url_map)

###############
#  blueprint  #
###############

@bp_base.route('/base/')
def base():
    return 'blue print test'

#######################
#  route params type  #
#######################

@bp_base.route('/params/<strparam>')
def param_str(strparam):
    return type(strparam)

@bp_base.route('/params/<int:intparam>')
def param_int(intparam):
    return type(intparam)

@bp_base.route('/params/<float:floatparam>')
def param_float(floatparam):
    return type(floatparam)


#################
#  route rules  #
#################
# /project  /project/
@bp_base.route('/project/')
def route_end():
    return 'hello'

#/about
@bp_base.route('/about')
def route_no_end():
    return 'hello2'

##########################
#  http mehtod post/get  #
##########################
#default get

@bp_base.route('/methods/', methods=['GET', 'POST'])
def methods():
    args = request.args if request.method == 'GET' else request.form
    print args
    if request.method == 'POST':
        return 'POST'
    else:
        return 'GET'

#####################
#  static filepath  #
#####################

@bp_base.route('/static/')
def static():
    return url_for('static', 'teststatic.css')


#####################
#  render template  #
#####################
'''
在模板内部你也可以访问 request 、session 和 g [1] 对象，以及 get_flashed_messages() 函数
'''

@bp_base.route('/hello/')
@bp_base.route('/hello/<name>')
def render_hello(name=None):
    return render_template('hello.html', name=name)


#################
#  file upload  #
#################
# form -> enctype="multipart/form-data"

@bp_base.route('/upload', methods=['POST'])
def upload():
    f = request.form['the_file']
    f.save('/tmp/path/' + secure_filename(f.filename))


############
#  cookie  #
############

@bp_base.route('/getcookie')
def get_cookies():
    username = request.cookies.get('username')
    return username

@bp_base.route('/writecookie')
def set_cookies():
    res = make_response('hello world')
    res.set_cookie('username', 'the_user_name')
    return res

#############
#  redirect #
#############

@bp_base.route('/redirect')
def redirect_url():
    return redirect(url_for('base'))

################
#  define 404  #
################

@bp_base.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


#############
#  session  #
#############

@bp_base.route('/session')
def session_op():
    if 'username' in session:
        print "session username"
    session['pwd'] = 12345
    session.pop('username', None)
    return 'session test'







