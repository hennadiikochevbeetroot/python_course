import math
from typing import Callable


def cylinder_volume_func(radius: int | float) -> Callable:
    partial_calculation = math.pi * (radius ** 2)
    print('Partial calculation: ', partial_calculation)

    def volume_func(height: int | float) -> float:
        print('Finishify calculation: ')
        return partial_calculation * height

    return volume_func


radius_10_cylinder_volume = cylinder_volume_func(10)
print('SPLITTER')
print(radius_10_cylinder_volume(25))

# print(radius_10_cylinder_volume(40))

# print(cylinder_volume_func(20)(50))
