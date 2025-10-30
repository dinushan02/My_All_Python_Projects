# 🎯 Number Guessing Game
# This game allows the user to guess a number between 1 and 100.
# The computer gives hints until the correct number is guessed.

import random

def number_guessing_game():
    # Generate a random secret number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        # Get user input and convert it to an integer
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Compare user's guess with the secret number
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            break

# Run the game
number_guessing_game()
