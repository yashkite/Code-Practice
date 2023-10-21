more_bids = True
bids = {}
while more_bids:
    choice = input("Is there more bids, y or n :- ")
    if choice == "y":
        name = input("Enter the biders name:- ")
        bid = int(input("Enter the bid amount:- "))
        bids[name] = bid
    else:
        more_bids = False
 
 
win_bid = max(bids.values())
winner = ""
tup_bid = bids.items()
for key, value in tup_bid:
    if value == win_bid:
        winner = key
print(f"The Winner is {winner} with the bid amount of {win_bid}")
