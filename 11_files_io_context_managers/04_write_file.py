# File opening modes:
# https://www.tutorialspoint.com/python/python_files_io.htm

file_name = './output4.txt'
with open(file_name, 'w') as fd:
    for number in range(10):
        fd.write(f'Number {number}\n')
