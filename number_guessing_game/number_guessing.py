def guess_number():
    while True:
        try:
            number_guessing = int(input("enter number: "))
        except ValueError:
          print("invalid number")
guess_number()
              