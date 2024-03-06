
hi_str = "Hello world!"
print(hi_str)
print(len(hi_str))

print("\nGet first character...")
print(hi_str[0])

print("\nGet last character...")
print(hi_str[-1])
print(hi_str[11])

print()
print(hi_str[2:5]) # to get the 3rd, 4, 5th characters
print(hi_str[6:])
print(hi_str[-3:])
print(hi_str[:5])

extra_spaces_str = "   Bob           "
print(len(extra_spaces_str)) # To see length of space
print(extra_spaces_str.strip())
print(len(extra_spaces_str.strip())) # To see length of space

example_str = "Here's some Text, with lots of Text!"
print(example_str)
# Count how many times substring occurs in a string
print(example_str.count("text"))
print(example_str.count("Text"))
print(example_str.count(" "))
print(example_str.count("e"))
print(example_str.count("t"))

# Changing the case
print(example_str.lower())
print(example_str.upper())
print(example_str.capitalize())

# Replace method
print(example_str.replace("Text", "words"))
print(example_str.replace("e", "z"))
