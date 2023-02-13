#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for letter in range(0, nr_letters):
  password += letters[random.randint(0, len(letters)-1)]
  # password += random.choice(letters)
  # Alternative method which is technically more efficient?

for symbol in range(0, nr_symbols):
  password += symbols[random.randint(0, len(symbols)-1)]

for number in range(0, nr_numbers):
  password += numbers[random.randint(0, len(numbers)-1)]

print(password)
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

length = range(0, len(password))
randomized = random.sample(length, len(password))
new_password = ""
for character in range(0, len(password)):
  new_password += password[randomized[character]]

print(new_password)

password_list = []
for char in range(0 , len(password)):
  password_list.append(password[char])

random.shuffle(password_list)

new_password2 = ""
for char in password_list:
  new_password2 += char

print(new_password2)
