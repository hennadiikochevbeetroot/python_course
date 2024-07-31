# Load - into python object, from json-valid formats

import json

json_filename = './output7.json'
with open(json_filename) as json_fd:
    json_object = json.load(json_fd)

print(json_object, type(json_object))
print(json_object['Key1'])
