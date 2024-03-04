# TASK: Waiter Helper

# Rationale: To practice lists
# Script should act like a waiter at a restaurant taking orders

# level 1

# Greet the user
print("Welcome to our Italian restaurant!")

# Print a list of starters
starters = ["Bread sticks", "Salad", "Garlic Bread"]
print("Starters:", starters)

# Take an input for the user for their starter
starter_choice = input("Please choose a starter: ").lower()

# Print a list of mains
mains = ["Pizza", "Spaghetti", "Lasagna"]
print("\nMain Courses:", mains)

# Take an input for the user for their main course
main_choice = input("Please choose a main: ").lower()

# Print a list of desserts
desserts = ["Icecream", "Cupcake", "Pudding"]
print("\nDesserts:", desserts)

# Take an input for the user for their dessert
dessert_choice = input("Please choose a dessert: ").lower()

# Print all of the user's choices
print("\nYour Order:")
print(f"Starter: {starter_choice}, Main Course: {main_choice}, ", "Dessert: {dessert_choice}")

# level 2
# Use at least one f-string
# Add each item ordered to a list called 'customer_order_list'
customer_order_list = (starter_choice, main_choice, dessert_choice)
print("Customer order list:", customer_order_list)
# if time: level 3 (may need research if we have not covered dictionaries yet)
# Use dictionaries and assign prices to the items. Create a bill at the end of the program.

# if time: level 4
# Add more to this program. Recommended ways are: Only allow input that is within the list, Add quantities of order etc.
