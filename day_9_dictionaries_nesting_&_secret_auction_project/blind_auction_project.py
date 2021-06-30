from os import system
# HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

bids = {}
bidding_finished = False


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other users wants to bid? type 'yes' or 'no' ")
    if should_continue == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif should_continue == "yes":
        # for windows os
        system('cls')
        # for mac and linux os
        system('clear')
