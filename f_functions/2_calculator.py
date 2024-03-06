# Using modules, return then print function!
# Create functions to add two numbers, subtract two numbers, multiply two numbers and divide two numbers.

from g_libraries_modules_packages import math_operations

def add(num1, num2):
    return math_operations.add(num1, num2)

def subtract(num1, num2):
    return math_operations.subtract(num1, num2)

def multiply(num1, num2):
    return math_operations.multiply(num1, num2)

def divide(num1, num2):
    return math_operations.divide(num1, num2)

print(add(15,5))
print(subtract(15,5))
print(multiply(15,5))
print(divide(15,5))
