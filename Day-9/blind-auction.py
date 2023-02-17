from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
bidders = 'yes'
auction = {}
name = ""
bid = 0
while bidders == 'yes':
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  auction[name] = bid
  clear()

currentbid = 0
winner = ""
for name in auction:
  if auction[name] > currentbid:
    currentbid = auction[name]
    winner = name

print(f"The winner is {winner} with a bid of ${currentbid}")
