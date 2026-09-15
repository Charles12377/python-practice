from employee import Employee
import pytest

@pytest.fixture
def employee():
    employee=Employee('wang','wei',1000000)
    return employee

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.salary == 1500000
    assert employee.name == 'wang wei'

def test_give_custom_raise(employee):
    employee.give_raise(1000000)
    assert employee.salary == 2000000