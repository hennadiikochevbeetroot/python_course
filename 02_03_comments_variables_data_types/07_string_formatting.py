
name = 'John'
surname = 'Smith'
skill = 'programming'


# Oldest way - and badly readable
print('My name is %s %s and I am skilled at %s' % (name, surname, skill))
print('I am %d years old' % 25)

# A little bit better way
print('My name is {} {} and I am skilled at {}'.format(name, surname, skill))
print('My name is {2} {1} and I am skilled at {0}'.format(skill, surname, name))

# The best way - the most modern
print(f'My name is {name} {surname} and I am skilled at {skill}')


