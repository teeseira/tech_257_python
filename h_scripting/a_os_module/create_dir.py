import os

# Home dir
home_dir = os.path.expanduser("~")

# Parent dir relative to the home dir
parent_dir = "Documents/github/tech_257_python/h_scripting/a_os_module"

# Desired directory name
directory = "test_dir"

# Full path
path = os.path.join(home_dir, parent_dir, directory)
print(path)

# Create the dir
os.mkdir(path)
