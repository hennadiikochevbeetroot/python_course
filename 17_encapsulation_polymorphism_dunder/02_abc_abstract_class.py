import abc


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
    pass
