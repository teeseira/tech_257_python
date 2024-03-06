# Write a Python script to calculate the user's year of birth.

# First Part
# define the a_variables age_int and name_str (set dummy/default/initial values)
# make a calculation for the year in which the person was born
# print out "OMG , you are years old so you were born in " with the correct values

#Second Part
# prompt the user for inputs and assign the variable age_int and name_str
# remove the initial values set

name_str = input("Enter your name: ")
age_str = input("Enter your age: ")
dob = 2024-int(age_str)
print(f"OMG, you are {age_str} years old so you were born in {dob}.")

# Third Part
# Calculate and print out the total number of hours this person has lived
hours_in_day = 24
days_in_year = 365
total_hours_lived = int(age_str) * days_in_year * hours_in_day
print(f"Total number of hours lived: {total_hours_lived}")

birthday_passed = input("Has your birthday happened this year? (Type either 'yes' or 'no': ").lower()

if birthday_passed == "yes":
    total_hours_lived = int(age_str) * days_in_year * hours_in_day
else:
    total_hours_lived = (int(age_str) - 1) * days_in_year * hours_in_day

# Output the total number of hours lived
print(f"{name_str} has lived approximately {total_hours_lived:,} hours.")