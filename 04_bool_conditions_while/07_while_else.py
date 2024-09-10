# While else is RARELY used , but is possible to check
# that break statement was not executed during the while loop


# Example
back_counter = 5
while back_counter > 0:
    back_counter -= 1
    if back_counter == 3:
        print('back_counter is three')
        break

    if back_counter == 4:
        print('back_counter is four')
        continue

    print(f'Current counter: {back_counter}')
else:
    print('Break was not executed')


