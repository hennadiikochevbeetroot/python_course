import math
from typing import Callable


def cylinder_volume_func(radius: int | float) -> Callable:
    def volume_func(height: int | float) -> float:
        print(f'Equation: V = {round(math.pi, 2)} * {height} * ({radius} ** 2)')
        return math.pi * height * (radius ** 2)

    return volume_func


radius_10_cylinder_volume = cylinder_volume_func(10)
print(radius_10_cylinder_volume(25))

