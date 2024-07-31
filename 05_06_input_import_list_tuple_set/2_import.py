# Most used libraries in coding
# import random
from random import randint as ri

# import random as r

print('Random number from 1 to 10: ', ri(1, 10))
# print('Random from 0 to 1: ', random.random())
# print('Random number taken from list:', random.choice([1, 2, 3, 4]))

import math
from math import sqrt

number = 25
print(f'Given number: {number}')
print('Square root: ', math.sqrt(number))
print('Sinus: ', math.sin(number))
# print("Math operation: ", math.)
print('Pi number: ', math.pi)
print('E number: ', math.e)

import os

print('PATH values: ', os.environ)
print('Current directory: ', os.getcwd())
print('Current user: ', os.getlogin())
print('Cpu count: ', os.cpu_count())

import sys

print('System platform: ', sys.platform)
print('Python version: ', sys.version)
print('Version differently: ', sys.version_info)
print('Command line argument number 2 (index 1): ', sys.argv[4])



