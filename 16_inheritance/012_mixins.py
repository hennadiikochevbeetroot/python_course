from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    model: str


class CargoMixin:
    def __init__(self):
        self.cargo_weight = 0

    def add_cargo(self, cargo_weight: int):
        self.cargo_weight += cargo_weight

    def remove_cargo(self, cargo_weight: int):
        self.cargo_weight -= cargo_weight

    def print_cargo_amount(self):
        print(f'Amount of cargo: {self.cargo_weight}')


class Hatchback(Car, CargoMixin):
    def __init__(self, brand: str, model: str):
        Car.__init__(self, brand, model)
        CargoMixin.__init__(self)


h = Hatchback('Toyota', 'Rav4')
h.add_cargo(50)
h.print_cargo_amount()
