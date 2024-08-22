from classes_to_test import Employee, EmployeeDatabase
import unittest


# employee = Employee('Jane', 'Air', 25, 123456)

class TestEmployee(unittest.TestCase):
    FIRST_NAME = 'John'
    LAST_NAME = 'Smith'
    AGE = 32
    SALARY = 123456

    def setUp(self):
        self.employee1 = Employee(self.FIRST_NAME, self.LAST_NAME, self.AGE, self.SALARY)
        self.employee2 = Employee('Jane', 'Air', 25, 123456)

        # In real-life we would instantiate smth like a db connection here.
        self.employee_db = EmployeeDatabase(self.employee1, self.employee2)

    def tearDown(self):
        # In real-life we would cleanup a temporary db
        self.employee_db.remove_all_employees()

    def test_employee_fields(self):
        self.assertEqual(self.employee1.first_name, self.FIRST_NAME)
        self.assertEqual(self.employee1.last_name, self.LAST_NAME)
        self.assertEqual(self.employee1.age, self.AGE)
        self.assertEqual(self.employee1.salary, self.SALARY)

    def test_employee_methods(self):
        self.assertEqual(self.employee1.full_name, f'{self.FIRST_NAME} {self.LAST_NAME}')

    def test_employee_salary_negative(self):
        with self.assertRaises(ValueError) as raise_context:
            self.employee1.salary = -1343434

        self.assertEqual(str(raise_context.exception), 'Salary cannot be negative')

    def test_employee_salary_increase(self):
        increase = 20000
        self.employee1.give_raise(increase)
        self.assertEqual(self.employee1.salary, self.SALARY + increase)

        self.employee2.give_raise(increase)
        self.assertEqual(self.employee2.salary, 123456 + increase)

    def test_salary_reasonable(self):
        self.assertTrue(self.employee1.is_salary_reasonable(self.employee1.salary))

        self.employee1.give_raise(10 ** 10)
        self.assertFalse(self.employee1.is_salary_reasonable(self.employee1.salary))

    def test_company_name(self):
        new_company_name = 'NewTechCorp'
        Employee.change_company_name(new_company_name)
        self.assertEqual(Employee.company_name, new_company_name)
        self.assertEqual(self.employee1.company_name, new_company_name)
        self.assertEqual(self.employee2.company_name, new_company_name)


if __name__ == '__main__':
    unittest.main()
