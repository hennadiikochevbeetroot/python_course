import math


class Cylinder:
    def __init__(self, height: int | float, radius: float):
        self.__height = height  # Making field private - non-accessible by default
        self.__radius = radius

    def __rounded_pi(self):
        return round(math.pi, 2)

    @property
    def volume(self):
        return self.__rounded_pi() * self.__radius ** 2 * self.__height

    # volume = lambda self: self.__rounded_pi() * self.__radius ** 2 * self.__height


cylinder = Cylinder(4, 5)
print(cylinder.volume)
# Below fields and method are not intended to be used, so they are not accessible
# print(cylinder.__height) - wouldn't work
# print(cylinder.__radius) - wouldn't work
# print(cylinder.__rounded_pi()) - wouldn't work

print('Hack which allows to get private properties')
print(cylinder._Cylinder__height)
print(cylinder._Cylinder__radius)


print(cylinder.__dict__)