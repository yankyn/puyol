from sqlalchemy import Integer, Column, String, and_
from sqlalchemy.orm import relationship, class_mapper
from sqlalchemy.orm.base import _entity_descriptor
from sqlalchemy.orm.relationships import RelationshipProperty
from sqlalchemy.sql.schema import ForeignKey
from puyol.orm.base import AlchemyBase, Base

__author__ = 'USER'


def make_criteria_from_kwargs(comparator, kwargs):
    # Copied from SA code for "any".
    return [getattr(comparator.property.mapper.class_, kwarg) == value
            for kwarg, value in kwargs.iteritems()]


class EachComparator(RelationshipProperty.Comparator):
    def each(self, criterion=None, **kwargs):
        clauses = make_criteria_from_kwargs(self, kwargs)
        clauses = clauses + [criterion] if criterion is not None else clauses
        return (~self.any(~and_(*clauses))) & (
            self.any(and_(*clauses))) if clauses else self.any()


class Country(Base, AlchemyBase):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String, name='name2')

    universities = relationship('University', comparator_factory=EachComparator)

    def foo(self):
        pass

    @property
    def name_and_id(self):
        return self.name, self.id


class University(Base, AlchemyBase):
    __tablename__ = 'universities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country_id = Column(ForeignKey(Country.id))

    country = relationship('Country', uselist=False)
    country = relationship('Country', uselist=False)
    courses = relationship('Course')


class Student(Base, AlchemyBase):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Course(Base, AlchemyBase):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    university_id = Column(ForeignKey(University.id))

    university = relationship('University')


class StudentCourseRelations(Base, AlchemyBase):
    __tablename__ = 'student_course_relations'

    student_id = Column(ForeignKey(Student.id), primary_key=True)
    course_id = Column(ForeignKey(Course.id), primary_key=True)
