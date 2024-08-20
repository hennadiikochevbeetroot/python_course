from typing import Generator


def power_of_three(max_power: int = 5) -> Generator[int, None, None]:
    current_power = 0
    while current_power < max_power:
        yield 3 ** current_power  # it will yield and remember current state
        current_power += 1


gen = power_of_three()
print(next(gen))
print(next(gen))
print(next(gen))

print('-------------------------------')
for current_power, three_in_power in enumerate(power_of_three(10)):
    print(f'3 in power {current_power} is {three_in_power}')
