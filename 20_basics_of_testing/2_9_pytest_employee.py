from classes_to_test import Employee, EmployeeDatabase
import pytest


@pytest.fixture()
def employee_db() -> EmployeeDatabase:
    employee1 = Employee('John', 'Smith', 32, 123456)
    employee2 = Employee('Jane', 'Air', 25, 123456)

    db = EmployeeDatabase(employee1, employee2)
    return db


@pytest.fixture()
def employee() -> Employee:
    return Employee('John', 'Smith', 32, 123456)


# We can also group tests in classes for readability
class TestEmployee:
    def test_employee_fields(self, employee):
        assert employee.first_name == 'John'
        assert employee.last_name == 'Smith'
        assert employee.age == 32
        assert employee.salary == 123456

    def test_employee_methods(self, employee):
        assert employee.full_name == 'John Smith'

    def test_employee_salary_negative(self, employee):
        with pytest.raises(ValueError) as exc_info:
            employee.salary = -1

        assert str(exc_info.value) == 'Salary cannot be negative'

    def test_employee_salary_increase(self, employee):
        increase = 20000
        employee.give_raise(increase)
        assert employee.salary == 123456 + increase

    def test_salary_reasonable(self, employee):
        assert employee.is_salary_reasonable(employee.salary) is True

        employee.give_raise(10 ** 10)
        assert employee.is_salary_reasonable(employee.salary) is False

    def test_company_name(self, employee):
        new_company_name = 'NewTechCorp'
        Employee.change_company_name(new_company_name)

        assert Employee.company_name == new_company_name
        assert employee.company_name == new_company_name
