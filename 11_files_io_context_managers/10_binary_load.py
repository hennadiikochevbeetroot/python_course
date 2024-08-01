# Binary data gets restored as it was saved

import pickle

binary_filename = './output9.bin'

with open(binary_filename, 'rb') as binary_fd:
    valuable_object = pickle.load(binary_fd)

timestamp = valuable_object['Current timestamp']

print(f'Timestamp: {timestamp}, type: {type(timestamp)}')
