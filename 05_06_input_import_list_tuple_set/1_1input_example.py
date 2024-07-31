input_num = input("Enter some integer: ")
while not input_num.isdigit():
    print('You have entered not an integer, please try again...')
    input_num = input("Enter some integer: ")

number = int(input_num)
print(number)
print(type(number))
if type(number) is int:
    print('Num is string')