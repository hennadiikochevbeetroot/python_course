# When reading a file in try-except:
# Always put close into finally clause
# It would ensure file is closed at the end
# (Best practice)

file_name = './text_file.txt'
fd = None
try:
    fd = open(file_name)
    print('Opened file')

    for symbol in fd.read():
        print('Symbol: ', symbol)
        if symbol.isdigit():
            print('Number divide by zero: ', int(symbol) / 0)

except ZeroDivisionError:
    print('Tried to divide by zero!')
finally:
    fd.close()
    print('Closed file')
