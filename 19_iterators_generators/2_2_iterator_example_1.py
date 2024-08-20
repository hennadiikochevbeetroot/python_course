class PowerThree:
    """Class to implement an iterator
    of powers of 3"""

    THREE = 3

    def __init__(self, max_power=0):
        self.max_power = max_power

    def __iter__(self):
        self.current_power = 0
        return self

    def __next__(self):
        if self.current_power <= self.max_power:
            result = self.THREE ** self.current_power
            self.current_power += 1
            return result

        raise StopIteration


numbers = PowerThree(3)
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))  # On this step if will not work, StopIteration


for current_power, power_three in enumerate(PowerThree(5)):
    print(f'3 to power {current_power} is {power_three}')
