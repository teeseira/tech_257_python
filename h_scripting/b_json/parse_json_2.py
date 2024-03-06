# Script that parses json

import json

path_to_json = "example_1.json"

json_file = json.loads(open(path_to_json).read())

for key in json_file:
    value = json_file[key]
    print(f"The key is {key} and the value is {value}")