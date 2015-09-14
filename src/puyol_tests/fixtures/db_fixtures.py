import pytest
import puyol

__author__ = 'USER'


def disconnect():
    puyol.disconnect()


@pytest.fixture(scope='function')
def db(request):
    puyol.connect()
    request.addfinalizer(disconnect)


@pytest.fixture
def country(db):
    co = puyol.Country(name='test')
    puyol.commit()
    return co


@pytest.fixture
def university_1(country):
    u = puyol.University(name='test1', country=country)
    puyol.commit()
    return u


@pytest.fixture
def university_2(country):
    u = puyol.University(name='test2', country=country)
    puyol.commit()
    return u
