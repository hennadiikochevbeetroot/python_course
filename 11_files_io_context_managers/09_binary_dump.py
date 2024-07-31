# Binary file can save any data

import datetime
import pickle

valuable_dict = {
    'Key1': 'Value1',
    'Prime number': 13,
    'Booleans': (True, False),
    'Nothing': None,
    'Current timestamp': datetime.datetime.now(),
}

binary_filename = './output9.bin'  # Extension does not matter
with open(binary_filename, 'wb') as binary_fd:
    pickle.dump(valuable_dict, binary_fd)
