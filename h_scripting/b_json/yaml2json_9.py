import json, os, sys, yaml # pip install pyyaml

# Checking if there is a file passed
if len(sys.argv) > 1:
    # opening the file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()
    else:
        print(f"ERROR {sys.argv[1]} not found")
        exit(1)
else:
    print(f"Usage: python yaml2json.py <source_yaml_file.yaml> <target_json_file.json>")

# Process the conversion - Use json library
converted_to_json = json.dumps(source_content)

# Save the conversion in a new file - output.json
with open("output.json", "w") as output_file:
    output_file.write(converted_to_json)
