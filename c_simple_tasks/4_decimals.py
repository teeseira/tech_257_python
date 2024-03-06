# Task: Use f-strings to format numbers

pi = 23.14159265359

# Use an f-string to print pi to 3 decimal places e.g. 'Pi to 3 decimal places: <value>'
print(f"Pi to 3 decimal places: {pi:.3f}")
# If you want 3 dp you need an "f", but if you want 3 places from the start ignore the f.
# print("Pi to 3 decimal places: {}".format(round(pi,3)))

# Use an f-string to print pi to 5 decimal places e.g. 'Pi to 5 decimal places: <value>'
print(f"Pi to 5 decimal values: {pi:.5f}") #use 5f
print(f"Pi to 5 decimals but no #f: {pi:.5}") #use 5f

score = 16
max_score = 26
score_as_decimal = score/max_score

# Use an f-string to print 'score_as_decimal' e.g. 'You scored 0.6153846153846154' (no % sign)
print(f"You scored {score_as_decimal}")

# Use an f-string to print 'score_as_decimal' formatted as a percentage e.g. 'You scored 61.538462%'
print(f"As a percentage, you scored {score_as_decimal*100:.6f}%")
# print(f"You scored {score_as_decimal:%}")

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to 2 decimal places e.g. 'You scored 61.54%'
print(f"As a percentage to 2 decimals, you scored {score_as_decimal*100:.2f}%")
# print(f"You scored {score_as_decimal:.2%}")

# Use an f-string to print 'score_as_decimal' formatted as a percentage to rounded to a whole number e.g. 'You scored 62%'
print(f"As a percentage rounded to whole, you scored {round(score_as_decimal*100)}%")
# print(f"You scored {score_as_decimal:.0%}")


