from sqlalchemy import event
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, mapper
import puyol
from puyol.orm.base import AlchemyBase

__author__ = 'USER'

DB_PATH = 'temp.db'


class NotConnectedException(Exception):
    pass


class ErrorRaiser(object):
    def __getattr__(self, attr):
        raise NotConnectedException()


engine = None
session = None
is_connected = None


@event.listens_for(mapper, 'init')
def auto_add(target, args, kwargs):
    global session
    session.add(target)


def disconnect():
    global engine, session, is_connected
    if engine:
        engine.dispose()
    session = ErrorRaiser()
    is_connected = False


def connect(db=None):
    global session, engine, is_connected
    if not is_connected:
        if not db:
            # Not currently used.
            db = DB_PATH
        engine = create_engine('sqlite://')
        session_factory = sessionmaker(bind=engine)
        session = session_factory()
        AlchemyBase.metadata.create_all(engine)


def commit():
    session.commit()


disconnect()
