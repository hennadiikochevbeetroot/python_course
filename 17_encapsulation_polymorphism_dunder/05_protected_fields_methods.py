

class Person:
    def __init__(self, name: str, age: int, is_married: bool = False):
        self.name = name               # public
        self.age = age                 # public
        self._is_married = is_married  # protected

    def __str__(self) -> str:
        return f'Person {self.name} age {self.age}, is married {self._is_married}'


class Worker(Person):
    def __init__(self, name: str, age: int, is_married: bool = False, specialty: str = 'Factory worker'):
        super().__init__(name, age, is_married)
        self._specialty = specialty

    def __str__(self) -> str:
        return f'{self._specialty} worker {self.name} age {self.age}'



person = Person('Billy', 42, True)
print(person)
print(person._is_married)    # Is possible to access, but not a best practice

print('--------------------------')

worker = Worker('Billy', 42, True)
print(worker)
print(worker._is_married)
print(worker._specialty)







