from art import logo
import random

print(logo)
number = random.randint(1, 100)
print(number)

EASY = 10
HARD = 5
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
if mode == "easy":
    print(f"You have {EASY} attempts remaining to guess the number")
    for i in range(EASY):
        attempts = 9
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You guessed correctly, the number is {number}.")
            exit()
        elif guess < number:
            print("Too Low")
            print(f"You have {attempts - i} attempts to guess the number.")
        elif guess > number:
            print("Too High")
            print(f"You have {attempts - i} attempts to guess the number.")

elif mode == "hard":
    print(f"You have {HARD} attempts remaining to guess the number")
    for i in range(HARD):
        attempts = 4
        guess = int(input("Make a guess: "))
        if guess == number:
            print(f"You guessed correctly, the number is {number}.")
            exit()
        elif guess < number:
            print("Too Low")
            print(f"You have {attempts - i} attempts to guess the number.")

        elif guess > number:
            print("Too High")
            print(f"You have {attempts - i} attempts to guess the number.")

else:
    print("Invalid Input.")
