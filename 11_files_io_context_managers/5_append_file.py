# Appending - adds content to existing
# Writing - rewrites the content


file_name = './output4.txt'
with open(file_name, 'a') as fd:
    for number in range(10):
        fd.write(f'Appending Number {number}\n')
