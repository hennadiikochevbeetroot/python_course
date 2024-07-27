# Decimal precision > float precision
from decimal import Decimal

a = 0.1
b = 0.2

product1 = 12.5
product2 = 12.5

result = Decimal('0.1') + Decimal('0.2')

print(float(a + b))
print(round(result, 25))
