# Dump - into text file - json-compatible formats
import datetime
import json

valuable_dict = {
    'Key1': 'Value1',
    'Prime number': 13,
    'Booleans': (True, False),
    'Nothing': None,
    'Current timestamp': datetime.datetime.now().isoformat(),
}

json_filename = './output7.json'
with open(json_filename, 'w') as json_fd:
    json.dump(valuable_dict, json_fd, indent=4)
