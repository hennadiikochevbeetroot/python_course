# Bool checking
all_truthy = all([True, 1, 'something'])
any_truthy = any([True, 1, 'something'])

# Execute any python code - not safe
eval('print("Hello")')

a = 1
a_hash = hash(a)
print(a_hash)

keys = ['key1', 'key2', 'key3']
values = ['val1', 'val2', 'val3']
zipped1 = zip(keys, values)

for pair in zipped1:
    print(pair)

zipped2 = zip(keys, values)
for key, value in zipped2:
    print(key, value)
