# Task: Mix all the data about a user into a list

# Prompt the user for inputs
name_str = input("Enter your name: ")
age_str = input("Enter your age: ")
dob_str = input("Enter your date of birth (YYYY-MM-DD): ")

# Mix the name, age, and DOB into one list user_details_list
user_details_list = [name_str, age_str, dob_str]

# Print the user's name, age, and DOB from the list
print("User details from the list:")
print("Name:", user_details_list[0])
print("Age:", user_details_list[1])
print("Date of Birth:", user_details_list[2])

# Check if age is saved as an integer in the list
if not user_details_list[1].isdigit():
    # Convert age to an integer
    age_int = int(age_str)
    # Add the age integer to the list
    user_details_list[1] = age_int

# Ask the user for their height in cm
height_str = input("Enter your height in cm: ")

# Save height as a float in the list
height_float = float(height_str)
user_details_list.append(height_float)

# Print the height from the list
print("Height:", user_details_list[-1])
