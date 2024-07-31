# Get input number
# Create a list
# Remove duplicates
# Calculate sum, min, max

import random

prompt = 'Please enter a number (from 1 to 10): '
while True:
    input_number = input(prompt)
    if input_number.isdigit() and 1 <= int(input_number) <= 10:
        break

number_to_generate = int(input_number)

number_set = set()
for _ in range(number_to_generate):
    generated_number = random.randint(1, 10)
    number_set.add(generated_number)

number_sorted_list = sorted(number_set)

print('Sorted List: ', number_sorted_list)
print('Sum: ', sum(number_sorted_list))
print('Max: ', max(number_sorted_list))
print('Min: ', min(number_sorted_list))
