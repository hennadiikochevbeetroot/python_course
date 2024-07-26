# Decimal precision > float precision
from decimal import Decimal

a = 0.1
b = 0.2

print(a + b)
print(Decimal('0.1') + Decimal('0.2'))
