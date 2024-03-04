# Task: Working with 'for loops'

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# Loop through list
print("1. Loop through list_data list:")
for num in list_data:
    print(num*2)

# Loop through embedded_lists
print("\n2. Loop through embedded_lists list:")
for data in embedded_lists:
    print(data)

# Loop through list embedded inside list
print("\n3. Loop through list inside list:")
for data in embedded_lists:
    print(data)
    for i in data:
        print(i)

# Loop through dictionary - keys only
print("\n4. Print dictionary keys:")
for key in dict_data:
    print(key)

# Loop through dictionary - values only
print("\n5. Print dictionary values:")
for key in dict_data:
    print(dict_data[key])

# Loop through dictionary value - values only
print("\n6a. Print values of a sub-dictionary:")
for key in dict_data:
    for value in dict_data[key].values():
        print(value)

print("\n6b. Print values of a sub-dictionary:")
for key in dict_data:
    nested_dict = dict_data[key]
    for embedded_value in nested_dict.values():
        print(embedded_value)

# Loop to print specific values of the dictionary items inside a dictionary
print("\n7. Print specific values of the dictionary items inside a dictionary:")
for key in dict_data:
    print(dict_data[key]["money"])

# Loop through a list with a nested if statement
print("\n8. Loop through a list with a nested if statement:")
for num in list_data:
    if num < 3:
        print("less than 3")
    elif num == 3:
        print("I found three")
    else:
        print("greater than 3")