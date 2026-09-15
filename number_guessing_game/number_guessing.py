import random

def guess_number(x, y):
    while True:
          try:
            to_int = int(input("enter number: "))
            if x <= to_int <= y:
                return to_int
            else:
                print(f"Out of range! Please enter a number between {x} and {y}.")
          except ValueError:
            print("invalid number")

def input_number():
    x = 1
    y = 100
    guessing = random.randint(x, y)
    
    print(f"I am thinking of a number between {x} and {y}.")
    counter = 0
    while True:
        input_guess = guess_number(x,y)
        counter += 1
        
        if input_guess < guessing:
            print("lesser number: try again")
        elif input_guess > guessing:
            print("greater number: try again")
        else:
            print(f"You win: it is the correct number in {counter} attempts")
            break
def main_game_loop():
    while True:
        
        input_number()

        play_again = input("\nplay again (y/n) ").strip().lower()
        if play_again != "y" or play_again != "yes":
            print("thanks for playing and goodbye")
            break
main_game_loop()