# Task: Using sets

# 1. Explain 2 main ways that sets are different to lists and tuples
# Sets contain only unique elements. If you try to add an element to a set that is already present, it won't be added again. This makes sets useful for tasks where you need to ensure that each element is unique. Lists and tuples, on the other hand, can contain duplicate elements.

#2. Create a set named 'fruits' containing "apple", "banana", and "cherry".
fruits = {"apple", "banana", "cherry"}

# 3. Print the set 'fruits'
print("Set:", fruits)

# 6. Add "orange" to the fruits set using one of the set's methods.
fruits.add("fruits")

# 5. Print the set 'fruits' - check it's added
print("New set after adding 'fruits':", fruits)

# 6. Remove "banana" from the fruits set using one of the set's methods.
fruits.remove("banana")

# 7. Print the set 'fruits' - check it's removed
print("New set after removing 'banana':", fruits)

# 8. Attempt to add another "apple" to the fruits set. What do you observe? Why does this happen?
fruits.add("apple")
print("New set after a second 'apple':", fruits)

#9. Print the 2nd item in the set. If there is any problem doing this, explain.
# print(fruits[1])
# Sets are unordered, so there is no concept of "second item" in a set.
# Therefore, it's not possible to directly access the second item in a set.
# If you need to access elements by index, you should use lists or tuples instead of sets.