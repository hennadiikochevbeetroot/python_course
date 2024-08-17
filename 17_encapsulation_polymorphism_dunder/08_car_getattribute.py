class Car:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    @property
    def prop(self):
        return 42

    def __getattribute__(self, item):
        print('Get attribute worked')

        if item in self.__dict__.keys():
            return super().__getattribute__(self, item)

        self.__dict__[item] = None
        return None


c = Car('Toyota', 'Land Cruiser')
print(c.brand)
# print(c.nonexisting)
