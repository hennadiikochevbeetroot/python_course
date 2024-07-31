# In with clause, we may several context managers at a time

input_filename = './text_file.txt'
output_filename = './output6.txt'

with open(input_filename) as input_fd, open(output_filename, 'w') as output_fd:
    for line_num, line in enumerate(input_fd.readlines(), 1):
        chars_amount = len(line.strip())
        message = f'Line {line_num} has {chars_amount} characters\n'
        output_fd.write(message)





