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
    def __init__(self, brand: str, model: str, color: str):
        self.car = Car(brand, model)
        self.bike = Bike(color)


g = Garage('Toyota', 'Land Cruiser', 'yellow')
print(g.car.drive())
del g
