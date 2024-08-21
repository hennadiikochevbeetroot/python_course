class Calculator:

    @staticmethod
    def add(num1: int | float, num2: int | float) -> int | float:
        return num1 + num2

    @staticmethod
    def subtract(num1: int | float, num2: int | float) -> int | float:
        return num1 - num2

    @staticmethod
    def multiply(num1: int | float, num2: int | float) -> int | float:
        return num1 * num2

    @staticmethod
    def divide(num1: int | float, num2: int | float) -> int | float:
        if num2 == 0:
            raise ZeroDivisionError('Num2 cannot be zero')

        return num1 / num2


class Employee:
    # Class attribute
    company_name = "TechCorp"

    def __init__(self, first_name, last_name, age, salary):
        # Instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age =
        self._salary = salary

    # Property to get the full name
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # Property to get the salary
    @property
    def salary(self):
        return self._salary

    # Property to set the salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    # Instance method to give a raise
    def give_raise(self, amount):
        self.salary += amount

    # Class method to change the company name
    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

    # Static method to check if a salary is reasonable
    @staticmethod
    def is_salary_reasonable(salary):
        return 30000 <= salary <= 200000
