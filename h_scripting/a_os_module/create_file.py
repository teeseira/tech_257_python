import os

# Create directory and path
home_dir = os.path.expanduser("~")
parent_dir = "Documents/github/tech_257_python/h_scripting/a_os_module"
directory = "test_dir"
path = os.path.join(home_dir, parent_dir, directory)

# Create filename and path
filename = "testfile2.txt"
filepath = os.path.join(path, filename)

# Make the file
with open(filepath, "w") as file:
    toFile = "Second file"
    file.write(toFile)
print(f"File {filename} created in {directory}")




