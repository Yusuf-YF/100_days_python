from random import randint

# print the logo
logo = """
+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+
|G|U|E|S|S| |T|H|E| |N|U|M|B|E|R|
+-+-+-+-+-+ +-+-+-+ +-+-+-+-+-+-+
"""
print(logo)



EASY_LEVEL = 10
HARD_LEVEL = 5
turns = 0


# make a function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == 'hard':
        return HARD_LEVEL
    else:
        return EASY_LEVEL


# make a function to check  user's guess against actual answer
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.\nGuess again.")
        return turns - 1
    elif guess < answer:
        print("Too low.\nGuess again.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


def game():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    # choosing a number between 1 to 100
    answer = randint(1, 100)

    # testing code
    print(f"Psst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0

    # repeat the guessing functionality if they get it wrong
    while guess != answer:
        # let the user to guess a number
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        # track the number of turns and reduce by 1 if they get it wrong
        if turns == 0:
            print(f"You've run out of guesses, you lose.")
            return



game()
