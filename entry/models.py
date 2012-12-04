from sqlalchemy import Column, Integer, String

from entry.database import Base

class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    text = Column(String(300))

    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text

    def __repr__(self):
        return '<Entry %s, %r>' % (self.id, self.title)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(30))
    
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %s, %r>' % (self.id, self.name)
