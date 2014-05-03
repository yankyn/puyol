from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from puyol.orm.base import AlchemyBase, Base

__author__ = 'USER'


class Country(Base, AlchemyBase):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String, name='name2')

    universities = relationship('University', backref="country")


class University(Base, AlchemyBase):
    __tablename__ = 'universities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    country_id = Column(ForeignKey(Country.id))


class Student(Base, AlchemyBase):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Course(Base, AlchemyBase):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    university_id = Column(ForeignKey(University.id))


class StudentCourseRelations(Base, AlchemyBase):
    __tablename__ = 'student_course_relations'

    student_id = Column(ForeignKey(Student.id), primary_key=True)
    course_id = Column(ForeignKey(Course.id), primary_key=True)
