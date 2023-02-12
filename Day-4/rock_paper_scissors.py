import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
hands = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp = random.randint(0, 2)

if choice >= 3 or choice < 0:
  print("You have entered an invalid number, you lose!")
else:
  print(hands[choice])
  print("Computer chose:")
  print(hands[comp])

  if choice + 1 == comp:
    print("You lose")
  elif choice + 2 == comp:
    print("You win")
  elif choice - 1 == comp:
    print("You win")
  elif choice - 2 == comp:
    print("You lose")
  else:
    print("It's a draw!")
  
