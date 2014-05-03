import pytest
import puyol

__author__ = 'USER'

@pytest.fixture
def disconnected():
    puyol.disconnect()


@pytest.fixture(params=[puyol.Country, puyol.Course, puyol.Student, puyol.University, puyol.StudentCourseRelations])
def cls(request):
    return request.param
