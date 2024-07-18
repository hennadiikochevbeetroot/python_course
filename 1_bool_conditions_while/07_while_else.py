# While else is RARELY used , but is possible to check
# that break statement was not executed during the while loop


back_counter = 5
while back_counter > 0:
    back_counter -= 1
    if back_counter == 3:
        print('back_counter is three')
        break

    print(f'Current counter: {back_counter}')
else:
    print('Break was not executed')


