from sqlalchemy.ext.declarative.api import declarative_base

__author__ = 'USER'

AlchemyBase = declarative_base()


class Base(object):

    @classmethod
    def get(cls, *args, **kwargs):
        from puyol.connector import session
        return session.query(cls, *args, **kwargs)
