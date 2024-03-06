# Task: Working with dictionaries

# 1. Create a dictionary called "student_1"
student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lessons": 4,
    "completed_lesson_names": ["a_variables", "data_types", "set up"]
}

# 3. Print the dictionary to the screen
print("This is the dictionary:", student_1)

# 4. Print its data type to the screen to check it's a dictionary
print("Data type of student_1 dict:", type(student_1))

# 5. Print the value for the key-value pair having the key "stream"
print("Value of the the key 'stream':", student_1["stream"])

# 6. Print the value for 'completed_lesson_names'
print("Value of completed_lesson_names:\n", student_1["completed_lesson_names"])

# 7. Print the data type for the value for 'completed_lesson_names'
print("Data type of completed_lesson_names value:\n", type(student_1["completed_lesson_names"]))

# 8. Print the first element/item in the list of 'completed_lesson_names'
print("First element of completed_lesson_names list:", student_1["completed_lesson_names"][0])

# 9. Change the value of "completed_lessons" to 3
student_1["completed_lessons"] = 3

# 9. Print the dictionary to check if the change was successful
print("Updated Dictionary:\n", student_1)

# 10. Delete "data_types" from the list under the key 'completed_lesson_names'
# del student_1["completed_lesson_names"][1]
student_1["completed_lesson_names"].remove("data_types")

# Use the keys() method on your dictionary to list all the keys
print("All keys in the dictionary:", student_1.keys())