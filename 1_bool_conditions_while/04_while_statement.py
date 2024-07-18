# While is the first loop we meet in Python
# `While` works while the condition given evaluates to True
# When condition becomes False, it stops

# Each execution of instructions inside of loop
# is called ITERATION.

threshold = 5
counter = 0
while counter < threshold:
    print(f'Counter value: {counter}, increase by 1')
    counter += 1

# Remember that we can
# combine conditions, loops, variables, comments, everything together

iterations_left = 3
reached_last_iteration = False
while iterations_left > 0:
    # To catch the moment of last iteration
    if iterations_left == 1:
        reached_last_iteration = True
        print('Last Iteration Ahead!')

    iterations_left -= 1
    print(f'Do some stuff, iterations left: {iterations_left}, {reached_last_iteration=}')



# If condition will be always True,
# then loop is going to be infinite

while True:
    print('Infinite iterations')


# If condition is False from start,
# then loop will not start

while False:
    print('False loop')

