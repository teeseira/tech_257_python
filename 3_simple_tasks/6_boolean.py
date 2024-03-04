# Task: Understanding 'None' in Python

# What is None in Python?
# In Python, None is a special constant representing the absence of a value or a null value. It is a singleton object of the NoneType class.

# When is it commonly used?
# None is commonly used to signify the absence of a value or to represent a default state. It is often used as a placeholder or default return value for functions that may not return a meaningful result under certain conditions.

# What's the equivalent in some other programming languages?
# In JavaScript, null serves a similar purpose to None in Python.
# In C and C++, NULL is used to represent a null pointer.

# Most important: What happens when you convert None to a boolean?
# When you convert None to a boolean, it evaluates to False.

# Write a piece of Python code to prove it
x = None
print(bool(x))  # Output will be False

# Write a piece of Python code to...
# assign x to be None
# print whether my variable x is equal to None

x = None
print(x == None)  # Output will be True
# print(x is None)