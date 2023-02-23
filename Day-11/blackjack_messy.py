import art
import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print(art.logo)
while game == 'y':
  your_cards = [random.choice(cards), random.choice(cards)]
  comp_cards = [random.choice(cards), random.choice(cards)]

  print(f"  Your cards: {your_cards}, current score: {sum(your_cards)}")
  print(f"  Computer's first card: {comp_cards[0]}")
  if sum(comp_cards) == 21:
    print(f"  Your final hand: {your_cards}, current score: {sum(your_cards)}")
    print(f"  Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
    print("You lose")
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    continue
  elif sum(your_cards) == 21:
    print(f"  Your final hand: {your_cards}, current score: {sum(your_cards)}")
    print(f"  Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
    print("You win")
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    continue
  
  card2 = input("Type 'y' to get another card, type 'n' to pass: ")
  while card2 == 'y':
    next_card = random.choice(cards)
    if next_card == 11 and (sum(your_cards) + 11) > 21:
      next_card = 1
    your_cards.append(next_card)
    if sum(your_cards) <= 21: 
      print(f"  Your cards: {your_cards}, current score: {sum(your_cards)}")
      print(f"  Computer's first card: {comp_cards[0]}")
      card2 = input("Type 'y' to get another card, type 'n' to pass: ")
    else:
      break

  if sum(your_cards) > 21:
    print(f"  Your final hand: {your_cards}, current score: {sum(your_cards)}")
    print(f"  Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
    print("You lose")
    game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    clear()
    print(art.logo)
    continue
  while sum(comp_cards) < 18:
    comp_cards.append(random.choice(cards))
  print(f"  Your final hand: {your_cards}, current score: {sum(your_cards)}")
  print(f"  Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")
  if sum(comp_cards) > 21:
    print("Opponent went over. You win 😁")
  elif sum(your_cards) > sum(comp_cards):
    print("You win")
  elif sum(your_cards) == sum(comp_cards):
    print("It's a draw!")
  else:
    print("You lose")
  
  game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  clear()
  print(art.logo)
  continue
