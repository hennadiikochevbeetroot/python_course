class Car:
    def __init__(self, brand: str, model: str, year: int, color: str):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.total_driven_km = 0

    def repaint(self, color: str):
        self.color = color

    def drive(self, driven_km: int):
        self.total_driven_km += driven_km

    def __str__(self) -> str:
        return (f'Car {self.brand} {self.model} \n'
                f'color {self.color} year {self.year} \n'
                f'mileage {self.total_driven_km}\n')


class Taxi(Car):
    DEFAULT_COLOR = 'Yellow'

    def __init__(self, brand: str, model: str, year: int):
        super().__init__(brand, model, year, self.DEFAULT_COLOR)
        self.current_passengers = 0

    def pickup_passengers(self, passengers_num: int) -> None:
        self.current_passengers += passengers_num

    def release_passengers(self, passengers_num: int) -> None:
        self.current_passengers -= passengers_num

    def __str__(self) -> str:
        return (f'Tax {self.brand} {self.model} year {self.year} \n'
                f'mileage {self.total_driven_km}\n'
                f'Passengers now: {self.current_passengers}')


# TODO: Lorry class example, multiple inheritance

taxi = Taxi('Daewoo', 'Lanos', 2000)
taxi.pickup_passengers(2)
taxi.drive(15)
print(taxi)
