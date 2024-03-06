# Script that parses yaml

import yaml

path_to_yaml = "output.yaml"

yaml_file = yaml.safe_load(open(path_to_yaml).read())

for key in yaml_file:
    value = yaml_file[key]
    print(f"The key is {key} and the value is {value}")
