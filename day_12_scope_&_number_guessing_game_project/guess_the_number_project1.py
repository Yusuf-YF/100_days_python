from art import logo
import random
from numbers import number

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

chosen_num = random.choice(number)

# Testing code
print(f'Psst, the correct answer is {chosen_num}.')

is_game_over = False

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    lives = 10
    while not is_game_over:
        guess = int(input("Make a Guess: "))
        # Check guessed number
        if guess == chosen_num:
            print(f"You got it! The answer was {guess}.!")
            is_game_over = True
        # Check if user is wrong
        elif guess < chosen_num:
            print("Too low.\nGuss again.")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number.")
            if lives == 0:
                print("You've run out of guesses, you lose.")
                is_game_over = True
        elif guess > chosen_num:
            print("Too high.\nGuss again.")
            lives -= 1
            print(f"You have {lives} attempts remaining to guess the number.")
            if lives == 0:
                print("You've run out of guesses, you lose.")
                is_game_over = True

elif difficulty == "hard":
    lives = 5
while not is_game_over:
    guess = int(input("Make a Guess: "))
    # Check guessed number
    if guess == chosen_num:
        print(f"You got it! The answer was {guess}.!")
        is_game_over = True
    # Check if user is wrong
    if guess < chosen_num:
        print("Too low.\nGuss again.")
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
        if lives == 0:
            print("You've run out of guesses, you lose.")
            is_game_over = True
    elif guess > chosen_num:
        print("Too high.\nGuss again.")
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
        if lives == 0:
            print("You've run out of guesses, you lose.")
            is_game_over = True
