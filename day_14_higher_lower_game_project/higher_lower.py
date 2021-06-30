from art import logo, vs
from game_data import data
import random
from os import system

def format_data(account):
    """Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'

# display art
print(logo)

score = 0

game_over = False

account_b = random.choice(data)

# make the game repeatable
while not game_over:

    # generate a random account from the game data
    # making account at position B become next account at position A
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    # ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    ## get follower account of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # clear the screen between rounds
    system("clear")
    print(logo)

    # give user feedback on their guess
    # score keeping

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_over = True
        print(f"Sorry, that's wrong. Final score: {score}")


