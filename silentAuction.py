participants = {}
print("Welcome to Silent Bidding....")
while(True):
    name = input("Enter your name: ")
    bid = int(input("Enter your bidding price: $"))
    participants[name]=bid
    playAgain = input("do you want to play again (y/n): ")
    if(playAgain.lower()=='n'):
        break
print(participants)
highestBid = 0
for val in participants.values():
    bid = val
    if(bid>highestBid):
        highestBid=bid
name = next(key for key,val in participants.items() if val == highestBid)
print(f"The winner of this bid is {name} with bidding of ${highestBid}")
