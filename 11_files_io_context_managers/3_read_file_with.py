# Better way to read files
# Without the need to close them manually
# Is to use Context Managers (`with` keyword)


file_name = './text_file.txt'
with open(file_name) as fd:
    for line_num, line in enumerate(fd.readlines(), 1):
        print(f'Line {line_num}: {line}', end='')
