# Bool checking
all_truthy = all([True, 1, 'something'])
any_truthy = any([True, 1, 'something'])



# Execute any python code - not safe
eval('print(all([True, 1]))')

a = 'string'
b = 'string'
print(hash(a))
print(hash(b))

keys = ['key1', 'key2', 'key3']
values = ['val1', 'val2', 'val3']
numbers = [1, 2]

zipped1 = zip(keys, values, numbers)
print(zipped1)

for line in zipped1:
    print(line)

zipped2 = zip(keys, values, numbers)
for key, value, number in zipped2:
    print(key, value, number)
