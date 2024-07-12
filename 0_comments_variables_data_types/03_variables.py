# We may assign any value to variable

a = 1
b = 'test string'
c = True
d = None
e = 5.6

print('Adding int and float: ', a + e)
print('B variable is: ', b)
print('Boolean C variable: ', c)
print(d)

# We may assign several variables in line
key1, key2 = 'a', 'b'
value1, value2, value3 = True, 3, 'string'

# Changing value of variable
value2 = value2 + 1
# OR, IN MORE READABLE WAY
value2 += 1

# We may use such changing with math operators
value2 -= 2
value2 *= 3
value2 /= 4
value2 //= 5
value2 **= 6

# In such way we can add strings
str_a = 'String A'
str_b = 'String B'
str_result = str_a + '    ' + str_b
print(str_result)
