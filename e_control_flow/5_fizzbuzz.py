# TASK: Fizz Buzz!

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# Function
'''
def fizz_buzz(num1,num2):
    for num in range(1,101):
        if num % num1 == 0 and num % num2 == 0:
            print("FizzBuzz")
        elif num % num1 == 0:
            print("Fizz")
        elif num % num2 == 0:
            print("Buzz")
        else:
            print(num)

fizz_buzz(1,16)
'''

'''
# using user input
print("\n --------------------------------------------")
num1 = int(input("Provide a number to be replaced for 'Fizz:' "))
num2 = int(input("Provide a number to be replaced for 'Buzz:' "))
for num in range(1,101):
    if num % num1 == 0 and num % num2 == 0:
        print("FizzBuzz")
    elif num % num1 == 0:
        print("Fizz")
    elif num % num2 == 0:
        print("Buzz")
    else:
        print(num)


'''








