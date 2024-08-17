import abc
from datetime import datetime, date


# Before abc module usage:
# Abstract classes and their methods/properties could be defined by
# raise NotImplementedError('Must be implemented in child class')

# Older standard (but you may consider it more readable)
class Parent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def some_method(self):
        """Some method docstring"""

    @abc.abstractproperty
    def prop(self):
        """Prop meaning docstring"""

    @abc.abstractclassmethod
    def class_method(cls):
        pass

    @abc.abstractstaticmethod
    def static_method():
        ...


# Newer standard - does all the same, and is more readable
class Parent(abc.ABC):
    @abc.abstractmethod
    def some_method(self):
        """Some method docstring"""

    @property
    @abc.abstractmethod
    def prop(self):
        """Prop meaning docstring"""

    @classmethod
    @abc.abstractmethod
    def class_method(cls):
        pass

    @staticmethod
    @abc.abstractmethod
    def static_method():
        ...


class Child(Parent):
    def some_method(self):
        pass

    @property
    def prop(self):
        pass

    @classmethod
    def class_method(cls):
        pass

    @staticmethod
    def static_method():
        pass


c = Child()
print(c)

if type(c) is Child:
    print('c is Child')

if isinstance(c, Child):
    print('c is instance Child')

if issubclass(Child, (Parent, abc.ABC)):
    print('Child is a subclass of parent')


def match_data(data):
    if type(data) is dict:
        return data.items()
    if type(data) is list:
        return [*data]
    if type(data) is set:
        return [*data]


def convert_date_to_string(param: datetime | date):
    if type(param) is date:
        return param.strftime('%Y-%m-%d')
    if type(param) is datetime:
        return param.strftime('%Y-%m-%d %H:%M:%S')


d = datetime(2024, 9, 1)
print(convert_date_to_string(d))
