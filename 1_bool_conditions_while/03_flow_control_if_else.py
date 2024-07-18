# We can control the flow of execution
# with `if` conditions
value_string = 'value'

# This will evaluate to True and execute
if value_string == 'value':
    print('Value string indeed is `value`')

# This will also evaluate to True and execute
if value_string != 'something':
    print('Value string is not `something`')

# But this will evaluate to False and NOT execute
if value_string == 'YES':
    print('Value string is `YES`')

# To execute something if condition didn't
# evaluate to True, we use `else`
if value_string == 'non-existing':
    print('Value string is `non-existing`')
else:
    print('Value string is not `non-existing`')

# To execute something with a different condition
# we use `elif` statement, and we may put any amount
# of them, whereas `if` and `else` can be only once
number = 3
if number == 1:
    print('Number is 1')
elif number == 2:
    print('Number is 2')
elif number == 3:
    print('Number is 3, at last')
else:
    print('Did not find correct number')

# If elif else with other comparisons
# And nested if elif else conditions will also work
# Nesting level is unlimited but better try
# keeping your code simple and understandable
new_number = 10
if new_number < 5:
    print('new_number is less than 5')
elif new_number % 3 == 0:
    print('new_number divides by 3 without remainder')
elif new_number >= 15:
    print('new_number is greater or equal than 15')
    if new_number == 15:
        print('new_number is exactly 15')
    else:
        print('new_number appeared to be strictly greater than 15')
else:
    print('new_number is some other case, no luck')
