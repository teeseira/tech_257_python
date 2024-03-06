import json, os, sys, yaml # pip install pyyaml

# Checking if there is a file passed
if len(sys.argv) > 1:
    # opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = json.load(source_file)
        source_file.close()
    else:
        print(f"ERROR {sys.argv[1]} not found")
        exit(1)
else:
    print(f"Usage: python json2yaml.py <source_json_file.json> <target_yaml_file.yaml>")

# Process the conversion - Use yaml library (1 line)
converted_to_yaml = yaml.dump(source_content)

# Save the conversion in a new file - output1.yaml (3 lines)
with open("output.yaml", "w") as output_file:
    output_file.write(converted_to_yaml)

