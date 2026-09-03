def get_guessing():

   guess_number = input("guess a number: ")
   while True:
    try:
      to_int = int(guess_number)
      if guess_number:
          return True
    except ValueError:
         print("invalid number")
get_guessing()