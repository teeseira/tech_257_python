# Task: Working with a list

# Create a list called 'shopping_list':
shopping_list = ['eggs', 'bread', 'bananas', 'biscuits', 'milk']

print("The shopping list:", shopping_list)

print("Data type of shopping_list:", type(shopping_list))

print("First item:", shopping_list[0])

print("Last item:", shopping_list[-1])

shopping_list[1] = 'rice'
print("Second item after change:", shopping_list[1])

# Add 'carrots' to the list
shopping_list.append('carrots')

print("List length after adding carrots:", len(shopping_list))

# Add another list with two items ('toffee' and 'coffee') to the 'shopping_list'
# shopping_list.extend(['toffee', 'coffee'])

another_list = ['toffee', 'coffee']
shopping_list = shopping_list + another_list
print("List after adding 2 items:", shopping_list)

# Remove "bananas" from list
shopping_list.remove('bananas')
print("List after removing bananas:", shopping_list)

# Remove the last item using the pop method
# You can also add a index to remove a specific index, leave empty to default remove last item
remove_item = shopping_list.pop()
print("Removed item (last item):", remove_item)
print("List after popping last item:", shopping_list)
