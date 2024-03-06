# pip install sys
import sys, os, subprocess, b_json

'''

# os
os.mkdir("test-dir")

# sys
if len(sys.argv) > 1:
    print("You gave me an argument!")

# subprocess
import subprocess
subprocess.run(["python", "hello_world.py"])


'''




# b_json

import b_json
x = { "name": "Ben",
      "age": 10,
      "city": "London"
}

y = b_json.dumps(x)

print("Print x:", x)
print("Type of x:", type(x))
print("Print y:", y)
print("Type of y:", type(y))
