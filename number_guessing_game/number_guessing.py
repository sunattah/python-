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
    
    max_attempts = 5 
    
    print(f"\nI am thinking of a number between {x} and {y}.")
    print(f"You have {max_attempts} attempts to guess it!")

    for attempt in range(max_attempts):
        print(f"\nAttempt {attempt + 1} of {max_attempts}:")
        input_guess = guess_number(x, y)
        
        if input_guess < guessing:
            print("lesser number: try again")
        elif input_guess > guessing:
            print("greater number: try again")
        else:
            print("You win: it is the correct number")
            return
            
    print(f"\nGame Over! You ran out of guesses. The correct number was {guessing}.")

def main_game_loop():
    while True:
        input_number()

        play_again = input("\nplay again (y/n) ").strip().lower()
        
        if play_again not in ["y", "yes"]:
            print("thanks for playing and goodbye")
            break

main_game_loop()
