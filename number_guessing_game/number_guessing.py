# import random

def guess_number():
    while True:
        try:
            # Added 'return' so the function actually gives the number back
            return int(input("enter number: "))
        except ValueError:
            print("invalid number")

def input_number():
    x = 1
    y = 100
    guessing = 42
    
    print(f"I am thinking of a number between {x} and {y}.")

    while True:
        # MOVED INSIDE THE LOOP: This asks the user for a new guess every turn
        input_guess = guess_number()
        
        if input_guess < guessing:
            print("lesser number: try again")
        elif input_guess > guessing:
            print("greater number: try again")
        else:
            print("You win: it is the correct number")
            break

input_number()
