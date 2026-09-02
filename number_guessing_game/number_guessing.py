guess_number = input("guess a number: ")
while True:
try:
    to_int = int(guess_number)
except ValueError:
        print("invalid number")