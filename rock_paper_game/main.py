def game():
    input_value = input("choose a value: ")
    print(input_value)
    if input_value != "scissor" or "paper":
        print("you loss the game")
    else:
        print("you win")
game()