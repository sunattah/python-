guess_number = input("guess a number: ")
try:
    to_int = int(guess_number)
except ValueError:
        print("invalid number")