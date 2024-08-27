from classes_to_test import Employee, EmployeeDatabase
import pytest


@pytest.fixture
def employee_db() -> EmployeeDatabase:
    employee1 = Employee('John', 'Smith', 32, 123456)
    employee2 = Employee('Jane', 'Air', 25, 123456)

    db = EmployeeDatabase(employee1, employee2)
    return db


@pytest.fixture
def employee() -> Employee:
    return Employee('John', 'Smith', 32, 123456)


# C++ 0.01 s
# Python 0.1 s


# We can also group tests in classes for readability
class TestEmployee:
    @staticmethod
    def test_employee_fields(employee):
        assert employee.first_name == 'John'
        assert employee.last_name == 'Smith'
        assert employee.age == 32
        assert employee.salary == 123456

    @staticmethod
    def test_employee_methods(employee):
        assert employee.full_name == 'John Smith'

    @staticmethod
    def test_employee_salary_negative(employee):
        with pytest.raises(ValueError) as exc_info:
            employee.salary = -1

        assert str(exc_info.value) == 'Salary cannot be negative'

    @staticmethod
    def test_employee_salary_increase(employee_db):
        increase = 20000
        # employee.give_raise(increase)
        # assert employee.salary == 123456 + increase
        employee1, employee2 = employee_db[0], employee_db[1]
        employee1_salary, employee2_salary = employee1.salary, employee2.salary

        employee1.give_raise(increase)
        assert employee1.salary == employee1_salary + increase

        employee2.give_raise(increase)
        assert employee2.salary == employee2_salary + increase

    @staticmethod
    def test_salary_reasonable(employee):
        assert employee.is_salary_reasonable(employee.salary) is True

        employee.give_raise(10 ** 10)
        assert employee.is_salary_reasonable(employee.salary) is False

    @staticmethod
    def test_company_name(employee):
        new_company_name = 'NewTechCorp'
        Employee.change_company_name(new_company_name)

        assert Employee.company_name == new_company_name
        assert employee.company_name == new_company_name
