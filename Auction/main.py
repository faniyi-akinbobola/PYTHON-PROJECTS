from art import logo

print(logo)
print("Welcome to the secret auction program.")
bidders = {}


def add_bidder(name, bid):
    bidders[name] = bid


def find_highest_bidder(bidders):
    highest_bid = 0
    winner = ""
    for key in bidders:
        bidders_amount = bidders[key]
        if bidders_amount > highest_bid:
            highest_bid = bidders_amount
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}.")


game_on = True
while game_on:
    name = input("What is your name? ")
    bid = float(input("What is your bid? $: "))
    add_bidder(name, bid)
    # print(bidders)
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if more_bidders == "no":
        game_on = False
        find_highest_bidder(bidders)