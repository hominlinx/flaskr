from entry import app

import os
current_dir = os.path.dirname(os.path.abspath(__file__))

#load settings
#FLASKR_SETTINGS = current_dir + os.sep + 'settings.py'
DATABASE = current_dir + os.sep + 'database/flaskr.db'
SQL_SRC = current_dir + os.sep + 'database/schema.sql'

DEBUG = False
SECRET_KEY = '?\xbf,\xb4\x8d\xa3"<\x9c\xb0@\x0f5\xab,w\xee\x8d$0\x13\x8b83'
USERNAME = 'admin'
PASSWORD = 'default'

app.config.from_object(__name__)
app.config.from_envvar("FLASKR_SETTINGS", silent=True)
#print app.config

app.run(debug=True)
