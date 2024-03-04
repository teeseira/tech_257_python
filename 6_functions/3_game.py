# Working on finishing this game:

```
def quiz_game():
    print("Welcome to the Interactive Quiz Game!")
    ready = input("Are you ready to play? (yes/no): ").lower()
    if ready != 'yes':
        print("Goodbye!")
        return

    questions = [
        ("What is 2 + 2?", "4"),
        ("Who is the current president of the United States?", "Biden"),
        ("What color is the sky?", "Blue")
    ]

    for question, answer in questions:
        user_answer = input(question + " ").capitalize()
        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")

quiz_game():
```