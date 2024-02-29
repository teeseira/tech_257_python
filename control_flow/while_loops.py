# Task: Using 'while loops' with an int

# Initialise x with the value of 0
x = 0

while x < 10:
    print(f"print x -> {x}")
    x += 1

# Initialize x again
x = 0

# Break while loop to exit when x equals 4
while x < 10:
    print(f"print x -> {x}")
    if x == 4:
        break
    x += 1
