# Why use f_functions?

# Principle: DRY (Don't Repeat Yourself)
# The variable to pass in the parentheses is called an argument not a parameter.

'''def print_something(print_string):
    print(print_string)
print_something("Hello")

def addition(int1, int2):
    return int1 + int2
print(addition(5,11))

def addition(int1=10, int2=200):
    return int1 + int2

print(addition())'''

def multi_args(*multiargs):
   print(type(multiargs))
   for arg in multiargs:
       print(arg)

multi_args(1, 2, 2, 3, 3, 4, 5, 5)

def greeting(name: str):
    print("\nHello, my name is " + name)

greeting("24601")