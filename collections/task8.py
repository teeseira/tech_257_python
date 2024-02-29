# Task: Using frozen sets

# 1. Create a frozen set named frozen_set containing elements "hello", "world".

frozen_set = frozenset(["hello", "world"])

# frozen_set = {"hello", "world"}
print(frozen_set)

# 2. Try to add "!" to frozen_set. What happens?

# frozen_set.add("!")
# print(frozen_set)

# 3. Create a normal set named normal_set containing elements "let's", "learn".

normal_set = {"let's", "learn"}

# 4. Try to add frozen_set to normal_set. Why does it work? Explain.

normal_set.add(frozen_set)

# 5. Print normal_set.
print(normal_set)

# Run your script half a dozen times. What do you notice about where frozen_set is added to normal_set? Hint: Look at the order of the items.
# What makes a frozen set different to a normal set? Explain.