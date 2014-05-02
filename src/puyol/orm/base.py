from sqlalchemy.ext.declarative.api import declarative_base
from puyol.orm.query import PuyolQuery

__author__ = 'USER'

AlchemyBase = declarative_base()


class Base(object):

    @classmethod
    def get(cls, *criteria, **kwargs):
        from puyol.connector import session
        return PuyolQuery(session.query(cls), cls, *criteria, **kwargs)