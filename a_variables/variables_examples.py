a = 1
b = 2.5
hi = "Hello World!"

print(type(a))
print(type(b))
print(type(hi))

x = 5
y = x # i.e. y = 5
z = 10

print("ID of x:", id(x)) # Output: some integer value
print("ID of y:", id(y)) # Output: the same integer value as id(x)
print("ID of z:", id(z)) # Output: another integer value (different from id(x))
