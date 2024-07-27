# Write a function that takes on an input random ints
# (between 1 and 10) and returns the longest consecutive run
# and the length of that run of elements of the list.
#
# func(1,2,2,3,4,4,4,4,4,9) -> 'Longest: number 4, times 5'
#

def get_longest_consecutive_run(*numbers: tuple[int]) -> str:
    curr_number, max_number = None, None
    curr_times, max_times = 0, 0

    for number in numbers:
        if curr_number == number:
            curr_times += 1
        else:
            if curr_times > max_times:
                max_times = curr_times
                max_number = curr_number

            curr_number = number
            curr_times = 1

    return f'Longest: number {max_number}, times {max_times}'


print(get_longest_consecutive_run(1,2,2,3,4,4,4,4,4,9))


