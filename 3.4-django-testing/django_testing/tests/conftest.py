import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args,**kwargs):
        return baker.model(Student,*args,**kwargs)
    return factory

@pytest.fixture
def course_factory():
    def factory(*args,**kwargs):
        return baker.model(Course,*args,**kwargs)
    return factory
