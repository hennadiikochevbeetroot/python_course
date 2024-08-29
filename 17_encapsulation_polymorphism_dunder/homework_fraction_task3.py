from __future__ import annotations

from math import gcd

# class Fraction:
# 	pass
#
# x = Fraction(1/2)
# y = Fraction(1/4)
#
# x + y == Fraction(3/4)


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def __str__(self):
        return f'{self.numerator} / {self.denominator}'

    @staticmethod
    def common_denominator(fraction1: Fraction, fraction2: Fraction):
        denom1, denom2 = fraction1.denominator, fraction2.denominator

        max_number = denom1 * denom2
        for common in range(1, max_number + 1):
            if common % denom1 == 0 and common % denom2 == 0:
                return common

        return max_number

    def simplify(self):
        # 72 / 9
        minimum = min(self.numerator, self.denominator)
        found_greatest = 1
        for number in range(1, minimum):
            if self.numerator % number == 0 and self.denominator % number == 0:
                found_greatest = number

        self.numerator //= found_greatest
        self.denominator //= found_greatest

    def __add__(self, other: Fraction):
        common_denom = self.common_denominator(self, other)
        numerator1 = (common_denom // self.denominator) * self.numerator
        numerator2 = (common_denom // other.denominator) * other.numerator
        sum_numerator = numerator1 + numerator2

        return Fraction(sum_numerator, common_denom)


# f1 = Fraction(1, 2)
# f2 = Fraction(1, 4)

f1 = Fraction(10, 24)
f2 = Fraction(22, 36)

print(f1 + f2)
