def celsius_to_fahrenheit(temperature: int | float) -> float:
    if temperature < 0:
        return -1

    # return temperature * 9 / 5 + 32
    step1 = temperature * 9
    step2 = step1 / 5
    step3 = step2 + 32

    return step3


fahr = celsius_to_fahrenheit(25)
print(fahr)
