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

    def __str__(self):
        return (f'Car {self.brand} {self.model} \n'
                f'color {self.color} year {self.year} \n'
                f'mileage {self.total_driven_km}\n')


car = Car('Daewoo', 'Lanos', 2000, 'green')
car.repaint('red')
car.drive(100)
car.drive(200)

print(car)
