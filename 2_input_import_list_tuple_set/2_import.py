# Most used libraries in coding
import random

print('Random number from 1 to 10: ', random.randint(1, 10))
print('Random from 0 to 1: ', random.random())
print('Random number taken from list:', random.choice([1, 2, 3, 4]))

import math

number = 25
print(f'Given number: {number}')
print('Square root: ', math.sqrt(number))
print('Sinus: ', math.sin(number))
print('Pi number: ', math.pi)
print('E number: ', math.e)

import os

print('PATH values: ', os.environ)
print('Current directory: ', os.getcwd())
print('Current user: ', os.getlogin())

import sys

print('System platform: ', sys.platform)
print('Python version: ', sys.version)
print('Version differently: ', sys.version_info)
