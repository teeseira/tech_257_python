# Task: Working with 'for loops'

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# Loop through list
print("Loop through list_data list:")
for num in list_data:
    print(num*2)

# Loop through embedded_lists
print("\nLoop through embedded_lists list:")
for data in embedded_lists:
    print(data)

# Loop through list embedded inside list
print("\nLoop through list inside list:")
for data in embedded_lists:
    print(data)
    for i in data:
        print(i)

# Loop through dictionary - keys only
print("\nPrint dictionary keys:")
for key in dict_data:
    print(key)

# Loop through dictionary - values only
print("\nPrint dictionary values:")
for key in dict_data:
    print(dict_data[key])

# Loop through dictionary value - values only
print("\nPrint values of a sub-dictionary:")
for key in dict_data:
    for value in dict_data[key].values():
        print(value)

# Loop to print specific values of the dictionary items inside a dictionary
print("\nPrint specific values of the dictionary items inside a dictionary:")
for key in dict_data:
    print(dict_data[key]["money"])

# Loop through a list with a nested if statement
print("\nLoop through a list with a nested if statement:")
for num in list_data:
    if num < 3:
        print("less than 3")
    elif num == 3:
        print("I found three")
    else:
        print("greater than 3")