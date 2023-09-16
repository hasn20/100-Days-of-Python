from art import logo
import os

bid_d = {}

def auction(Name_of_Bidder, Bid_Amount):
  new_key = Name_of_Bidder
  new_value = Bid_Amount
  bid_d[new_key] = new_value

print(logo)
print("Welcome To Secret Auction Program")




a = True

while a:
  name = input("What is your name ?: ")
  bid = input("What's your bid ?: $")
  auction(name, bid)
  again = input("Are there any other bidders 'yes' or 'no'")
  if again == "no":
    a = False
  else:
    os.system("cls")

high_auction = 0
high_key = None
for keys in bid_d:
  amount = int(bid_d[keys])
  if amount > high_auction:
    high_auction = amount
    high_key = keys

print(f"The winner is {high_key} with a bid of ${high_auction}")