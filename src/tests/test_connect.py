import puyol
from puyol.connector import ErrorRaiser

__author__ = 'USER'


def test_before_connect():
    from puyol.connector import session
    assert isinstance(session, ErrorRaiser)


def test_connect():
    puyol.connect()
    from puyol.connector import session
    assert not isinstance(session, ErrorRaiser)

