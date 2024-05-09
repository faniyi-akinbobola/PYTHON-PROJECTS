import  random
from art import  logo

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print(logo)
print("Welcome to Password Generator!")
num_of_letters = int(input("How many letters would you like your password to contain?: \n"))
num_of_numbers = int(input("How many numbers would you like your password to contain?: \n"))
num_of_symbols = int(input("How many symbols would you like your password to contain?: \n"))

password = ""
for i in range(num_of_letters):
    letter = random.choice(letters)
    password += letter

for i in range(num_of_numbers):
    number = random.choice(numbers)
    password += number

for i in range(num_of_symbols):
    symbol = random.choice(symbols)
    password += symbol

shuffled_password = ''.join(random.sample(password, len(password)))
print(f"Your generated password is {shuffled_password}")
