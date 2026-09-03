import random

def get_guessing():
    x = 1
    y = 100
    select_number = random.randint(x, y)
    for number_range in select_number:
       guess_number = input("guess a number: ")
       if guess_number  not in select_number:
        print("not the correct number")

       while True:
        try:
         to_int = int(guess_number)
         if guess_number:
          return True
        except ValueError:
         print("invalid number")
         break
get_guessing()