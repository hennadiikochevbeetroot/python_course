import json

some_dict = {
    "name": "Jonny",
    "age": 30,
    "is_student": True,
    "courses": ["Web Dev", "CP"]
}

# Dumps == dump dict/list into string
json_string = json.dumps(some_dict, indent=4)
print(json_string)

json_looking_string = '{"key": "value"}'


# Loads == load string into a dict/list
dict_from_json = json.loads(json_looking_string)
print(dict_from_json['key'])
