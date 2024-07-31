# Continue statement is used to skip one iteration
# of the loop (while, for)


threshold = 11
counter = 0
while counter < threshold:
    counter += 1
    if counter % 5 == 0:
        print(f'Skipping each fifth iteration, counter: {counter}')
        continue

    print(f'Business logic here, counter: {counter}')
