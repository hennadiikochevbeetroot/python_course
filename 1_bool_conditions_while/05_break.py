# Break statement is used to stop iterations
# before the loop ends by itself because of
# condition became False

big_threshold = 10000
counter = 0
while counter < big_threshold:
    print(f'Counter state: {counter}')
    if counter == 5:
        print('Counter became 5, let us stop execution')
        break
    counter += 1

print(f'Last counter value: {counter}')

# Break is also a good thing to stop the infinite loop

iterations_left = 5
while True:
    print(f'Doing some stuff, times left: {iterations_left}')
    iterations_left -= 1
    if iterations_left == 0:
        break
