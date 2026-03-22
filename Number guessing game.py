# Number guess game.
# This is intresting game.

import random

# Generate a random number

num = random.randint(1, 10)
tries = 0

print("Guess the number between 1 and 10!")

while True:
    try:
        guess = int(input("Enter your guess: "))
        tries += 1

        if guess == num:
            print(f"🎉 Correct! You guessed the number in {tries} tries.")
            break
        elif guess > num:
            print("⬇️ Go a little lower")
        else:
            print("⬆️ Go a little higher")
    except ValueError:
        print("❌ Please enter a valid number")
