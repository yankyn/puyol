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


def test_query():
    puyol.connect()
    [a for a in puyol.Country.get()]


def test_hybrid_property_object():
    country = puyol.Country(name='test')
    [a for a in country.universities]


def test_hybrid_property_class():
    print puyol.Country.get().join(puyol.Country.universities)
