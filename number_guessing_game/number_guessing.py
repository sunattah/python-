# import random

def guess_number():
    while True:
        try:
            return int(input("enter number: "))
        except ValueError:
            print("invalid number")

def input_number():
    x = 1
    y = 100
    guessing = 42
    
    print(f"I am thinking of a number between {x} and {y}.")
    counter = 0
    while True:
        input_guess = guess_number()
        
        if input_guess < guessing:
            counter += 1
            print("lesser number: try again")
        elif input_guess > guessing:
            print("greater number: try again")
            counter += 1
        else:
            print(f"You win: it is the correct number in {counter}")
            break

input_number()
