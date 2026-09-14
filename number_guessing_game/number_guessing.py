import random
def guess_number():
    while True:
        try:
            number_guessing = int(input("enter number: "))
        except ValueError:
          print("invalid number")
# guess_number
def input_number():
    x = 1
    y = 100
    guessing = random.randint(x, y)
    if guess_number < guessing:
        print("lesser number: try again")
        if guess_number > guessing:
            print("greater number: try again")
input_number()