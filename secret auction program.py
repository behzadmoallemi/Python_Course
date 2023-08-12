from replit import clear
bids = {}
biding_finished = False

def find_highest_bidder(bid_record):
    highest_bid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

print("Welcome to the secret auction program.")

while not biding_finished:
    name = input("What is your name?")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n")
    clear()
    if should_continue == "no":
        biding_finished = True
        find_highest_bidder(bids)
