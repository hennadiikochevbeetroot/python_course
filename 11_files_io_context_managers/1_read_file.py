# Typical flow:
# Open file -> read contents -> close file


file_name = './text_file.txt'
file_descriptor = open(file_name, 'r')   # 'r' is a default argument

for line in file_descriptor:
    print(line, end='')  # line already has \n ending, that's why we don't need newline by default

file_descriptor.close()
