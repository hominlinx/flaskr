from entry.database import init_db

init_db()

from entry.database import db_session
from entry.models import User
from entry.models import Entry

print User.query.all()
print Entry.query.all()
