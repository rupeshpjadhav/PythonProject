import random

print("Hello, let's play the guessing game!")

rand_num = random.randint(1, 100)
attempts = 0

while True:
    user_inp = input("Enter your guess or type q to quit: ").strip()

    # Check for the quit command before converting the input to a number.
    if user_inp.lower() == "q":
        print("You quit the game. Thanks for playing!")
        break

    # Convert the input to an integer; ask again if it isn't a valid number.
    try:
        user_inp = int(user_inp)
    except ValueError:
        print("Please enter a whole number or q to quit.")
        continue

    attempts += 1
    if user_inp < rand_num:
        print("Your guess is low; guess a higher number.")
    elif user_inp > rand_num:
        print("Your guess is high; guess a lower number.")
    else:
        print(
            f"Your guess is correct! You took {attempts} "
            "attempt(s)."
        )
        break
