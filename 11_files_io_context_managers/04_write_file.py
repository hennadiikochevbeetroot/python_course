# File opening modes:
# https://www.tutorialspoint.com/python/python_files_io.htm
import time

file_name = './output4.txt'
with open(file_name, 'w') as fd:
    for number in range(10):
        fd.write(f'Number {number}\n')


# fd = open(file_name, 'w')
# for number in range(10):
#     fd.write(f'Number {number}\n')
#
# fd.close()

for i in range(20):
    print(f'Sleeping {i} seconds')
    time.sleep(1)


