import pytest
import puyol

__author__ = 'USER'


def disconnect():
    puyol.disconnect()


@pytest.fixture(scope='function')
def db(request):
    puyol.connect()
    request.addfinalizer(disconnect)


@pytest.fixture()
def country(db):
    co = puyol.Country(name='test')
    puyol.commit()
    return co
