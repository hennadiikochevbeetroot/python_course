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

    def __init__(self, first_name: str, last_name: str, age: int, salary: int):
        # Instance attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self._salary = salary

    # Property to get the full name
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    # Property to get the salary
    @property
    def salary(self) -> int:
        return self._salary

    # Property to set the salary
    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError('Salary cannot be negative')
        self._salary = value

    # Instance method to give a raise
    def give_raise(self, amount) -> None:
        self.salary += amount

    # Class method to change the company name
    @classmethod
    def change_company_name(cls, new_name) -> None:
        cls.company_name = new_name

    # Static method to check if a salary is reasonable
    @staticmethod
    def is_salary_reasonable(salary) -> bool:
        return 30000 <= salary <= 200000


class EmployeeDatabase:
    def __init__(self, *employees: Employee):
        # Initialize an empty list to store employee objects
        self.__employees = []
        for employee in employees:
            self.add_employee(employee)

    def add_employee(self, employee):
        # Add an employee object to the database
        if isinstance(employee, Employee):
            self.__employees.append(employee)
        else:
            raise TypeError("Only Employee instances can be added")

    def remove_employee(self, employee):
        # Remove an employee object from the database
        if employee in self.__employees:
            self.__employees.remove(employee)
        else:
            raise ValueError("Employee not found")

    def remove_all_employees(self):
        self.__employees = []

    def get_all_employees(self):
        # Return a list of all employee objects
        return self.__employees

    def __getitem__(self, index):
        return self.__employees[index]

    def find_employee_by_name(self, first_name, last_name):
        # Find an employee by their full name
        for employee in self.__employees:
            if employee.first_name == first_name and employee.last_name == last_name:
                return employee
        raise ValueError("Employee not found")
