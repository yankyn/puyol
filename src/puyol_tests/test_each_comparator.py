import puyol

__author__ = 'Yanky'

def test_each_on_empty_relationship(country):
    assert not puyol.Country.get(
        puyol.Country.universities.each(name='some lie'))


def test_each_matches_all(country, university_1, university_2):
    assert puyol.Country.get(
        puyol.Country.universities.each(puyol.University.name.like('test%')))


def test_each_matches_one(country, university_1, university_2):
    assert not puyol.Country.get(
        puyol.Country.universities.each(id=university_1.id))


def test_each_matches_one_complex(country, university_1, university_2):
    assert not puyol.Country.get(
        puyol.Country.universities.each(puyol.University.name.like('test%'),
                                        id=university_1.id))
