class Container:
    def __init__(self, *values):
        self.__internal_list = [*values]

    def __getitem__(self, item):
        return self.__internal_list[item]


# c = Container(1,2,3,4,5)
# print(c[4])


class Car:
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

    # def __getattr__(self, item):
    #     print('If __getattr__ method worked')
    #     if item in self.__dict__:
    #         return self.__dict__[item]
    #
    #     self.__dict__[item] = None
    #     return self.__dict__[item]

    def __getattribute__(self, item):
        print('If __getattribute__ called')
        # if item in self.__dict__:
        #     return self.__dict__[item]
        # return dict(self.__dict__).get(item, None)

        if item == 'brand':
            return self.brand

        # self.__dict__[item] = None
        # return self.__dict__[item]


c = Car('BMW', 'Z4')
# print(c.__dict__)

# print(c.nonexisting)
print(c.brand)
