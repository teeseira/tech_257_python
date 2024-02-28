# Task: Finish the guessing game with string slicing

# Guess the word with 4 hints to help
# Rationale: Practice word slicing
# Type of exercise: Finish the code
original_word = "recommendation"
scrambled_word = "eoommandretnic"
# Create the hint slices...
# Create the word slice according to the clue below, use the format "original_word[x:y]"

# Game instructions
print("Scrambled word:", scrambled_word)
print("Guess the original word from the scrambled version.")

# Create hints based on list slicing,
hint1_slice = original_word[4:6] # 5th and 6th
print("Hint 1: 5th and 6th letters are: " + hint1_slice)
hint2_slice = original_word[-3:] # Last 3
print("Hint 2: Last 3 letters are: " + hint2_slice)
hint3_slice = original_word[7:10] # 8th to 10th
print("Hint 3: 8th to 10th letters are: " + hint3_slice)
hint4_slice = original_word[:2] # First 2
print("Hint 4: First two letters are: " + hint4_slice)
# Game ends here
print("What's your guess?")