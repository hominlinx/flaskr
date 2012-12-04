import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing

from entry.database import db_session
from entry.models import Entry

from entry.forms import LoginForm

import os
current_dir = os.path.dirname(os.path.abspath(__file__))

#rebuild: move to runserver.py
#db config
#DATABASE = current_dir + os.sep + '../database/flaskr.db'

# rebuild: move to settings.py
#DEBUG = True
#SECRET_KEY = 'development key'
#USERNAME = 'admin'
#PASSWORD = 'default'

#flask begin
#app = Flask(__name__)
from entry import app
  #from object

#rebuild: change to runserver.py
#app.config.from_object(__name__)
  #from config
#app.config.from_envvar('FLASKR_SETTINGS', silent=True)

#rebuild: use sqlalchemy
#db operations
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource(current_dir + os.sep + '../database/schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()
    
@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception=None):
    g.db.close()
    db_session.remove()

#entries operation
@app.route('/')
def show_entries():
    #rebuild: use sqlalchemy
    entries = Entry.query.all()
    entries = [dict(title=entry.title, text=entry.text) for entry in entries]

    #cur = g.db.execute('select title, text from entries order by id desc')
    #entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)

    #rebuild: use sqlalchemy
    entry = Entry(request.form['title'], request.form['text'])    
    db_session.add(entry)
    db_session.commit()
    #g.db.execute('insert into entries (title, text) values(?, ?)',
    #             [request.form['title'], request.form['text']])
    #g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        if form['username'].data != app.config['USERNAME']:
            error = 'Invalid username' 
        elif form['password'].data != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error, form=form)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run()
