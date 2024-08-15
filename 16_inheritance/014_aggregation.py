from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    model: str

    def drive(self):
        return f'Drives {self.brand} {self.model}'


@dataclass
class Bike:
    color: str


class Garage:
    def __init__(self, car: Car, bike: Bike):
        self.car = car
        self.bike = bike


c = Car('Toyota', 'Land Cruiser')
b = Bike('Yellow')

g = Garage(c, b)
print(g.car.drive())

c.model = 'Rav4'
print(g.car.drive())

del g



