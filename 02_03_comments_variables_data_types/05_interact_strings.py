# Length of string (in fact, of everything that may have length)
print(len('string test'))
print(len(''))

# String concatenation
print('Two' + ' ' + 'Words' + '!')
print('string' * 3)
print('string' + 'string' + 'string')

# String methods (accessed with . and triggers autocompletion)
s = 'Test_String'
print(s.count('s'))
print(s.upper())
print(s.lower())

s = s + 'More test'
print(s)

s += 'Even more'
print(s)

s.replace('more', 'less')
print(s)

number_string = '8776787'
print(number_string.isdigit())

# In operator
txt = 'Random words together'
print('word' in txt)
