import art
import random

def check_guess(guess, actual):
  if guess > actual:
    print("Too high!")
    return False
  elif actual > guess:
    print("Too low...")
    return False
  else:
    print("You actually got it?! You lucky bastard!")
    return True

def random_number():
  return random.randint(1, 100)

def guessordie():
  print(art.logo)
  print("Welcome to the Number Guessing Game! Your life depends on this.")
  print("I'm thinking of a number between 1 and 100.")
  actual = random_number()
  
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  
  if difficulty == 'easy':
    attempts = 10
  elif difficulty == 'hard':
    attempts = 5
  else:
    print('invalid input')
  
  while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    counter = check_guess(guess, actual)
    if counter == False:
      attempts -= 1
      if attempts == 0:
        print("You've run out of luck Cowboy. Bang!")
    else:
      break

guessordie()
