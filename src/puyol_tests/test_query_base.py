import pytest
import puyol
from puyol.connector import NotConnectedException
from puyol.orm.query import PuyolQuery

__author__ = 'USER'


def get_first_from_query(q):
    return q._q.first()


def test_query_cls(db, cls):
    assert isinstance(cls.get(), PuyolQuery)
    assert cls.get()._cls == cls


def test_query_disconnected(disconnected, cls):
    with pytest.raises(NotConnectedException):
        cls.get()


def test_query_refines_kwargs_positive(db, country):
    qu = puyol.Country.get(name=country.name)
    assert get_first_from_query(qu) == country


def test_query_refines_kwargs_negative(db, country):
    qu = puyol.Country.get(name='not' + country.name)
    assert not get_first_from_query(qu)


def test_query_refines_criterion_positive(db, country):
    qu = puyol.Country.get(country.name == country.name)
    assert get_first_from_query(qu) == country


def test_query_refines_criterion_negative(db, country):
    qu = puyol.Country.get(puyol.Country.name == 'not' + country.name)
    assert not get_first_from_query(qu)


def test_query_refines_criteria_negative_1(db, country):
    qu = puyol.Country.get(puyol.Country.name == country.name,
                           puyol.Country.id == country.id + 1)
    assert not get_first_from_query(qu)


def test_query_refines_criteria_negative_2(db, country):
    qu = puyol.Country.get(puyol.Country.name == 'not' + country.name,
                           puyol.Country.id == country.id)
    assert not get_first_from_query(qu)


def test_query_refines_criteria_positive(db, country):
    qu = puyol.Country.get(country.name == country.name,
                           puyol.Country.id == country.id)
    assert get_first_from_query(qu) == country


def test_query_refines_criterion_and_kwarg_negative_1(db, country):
    qu = puyol.Country.get(puyol.Country.name == country.name,
                           id=country.id + 1)
    assert not get_first_from_query(qu)


def test_query_refines_criterion_and_kwarg_negative_2(db, country):
    qu = puyol.Country.get(puyol.Country.name == 'not' + country.name,
                           id=country.id)
    assert not get_first_from_query(qu)


def test_query_refines_criterion_and_kwarg_negative_3(db, country):
    qu = puyol.Country.get(puyol.Country.id == country.id + 1,
                           name=country.name)
    assert not get_first_from_query(qu)


def test_query_refines_criterion_and_kwarg_negative_4(db, country):
    qu = puyol.Country.get(puyol.Country.id == country.id,
                           name='not' + country.name)
    assert not get_first_from_query(qu)


def test_query_refines_criterion_and_kwarg_positive_1(db, country):
    qu = puyol.Country.get(puyol.Country.name == country.name, id=country.id)
    assert get_first_from_query(qu) == country


def test_query_refines_criterion_and_kwarg_positive_2(db, country):
    qu = puyol.Country.get(puyol.Country.id == country.id, name=country.name)
    assert get_first_from_query(qu) == country
