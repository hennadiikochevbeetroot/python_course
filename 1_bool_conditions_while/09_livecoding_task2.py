# Task 2
# Write a Python program to construct the following pattern,
# using a while loop
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

star_counter = 1
tree_size = 20
star_symbol = '*'
while star_counter < tree_size:
    inner_counter = 0
    while inner_counter < star_counter:
        print(star_symbol, end=' ')
        inner_counter += 1

    star_counter += 1
    print()

while star_counter >= 1:
    inner_counter = 0
    while inner_counter < star_counter:
        print(star_symbol, end=' ')
        inner_counter += 1

    star_counter -= 1
    print()

