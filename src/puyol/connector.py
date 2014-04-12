from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
import puyol
from puyol.orm.base import AlchemyBase

__author__ = 'USER'

DB_PATH = 'temp.db'


class ErrorRaiser(object):

    def getattr(self, attr):
        raise NotImplementedError()

session = ErrorRaiser()
is_connected = False


def connect(db=None):
    global session
    global is_connected
    if not is_connected:
        if not db:
            db = DB_PATH
        engine = create_engine('sqlite://')
        session_factory = sessionmaker(bind=engine)
        session = session_factory()
        AlchemyBase.metadata.create_all(engine)
