# def player_choice():
#     while True:
#         input_value = input("enter your choice: ")
#         if input_value == "paper":
#             print("YOu inputed paper")
#             if input_value == "scissors":
#                 print("You inputed scissors")
#                 break
#             elif print("invalid input"):
#                 continue

            
# player_choice()

"""
Rock, Paper, Scissors
---------------------
Rules:
- The player and the computer each pick rock, paper, or scissors.
- rock beats scissors, scissors beats paper, paper beats rock.
- Same choice on both sides is a tie.
- Keep a running score (wins, losses, ties) across rounds.
- Ask to play again after each round.

Build it in order. Run and test after each step before moving on.
Fill in the blanks marked with `# TODO`.
"""

import random

CHOICES = ["rock", "paper", "scissors"]

# Step 4: what does each choice defeat?
# TODO: fill in the dictionary, e.g. "rock": <what rock beats>
BEATS = {"rock":"scissors",
         "scissors":"paper",
         
}


def get_player_choice():
    """
    Step 1: keep asking until the player types a valid choice.
    Return the choice as a lowercase string.
    Hint: .strip().lower() cleans the input, `in CHOICES` checks it.
    """
    while True:
        choice = input("rock, paper, or scissors? ").strip().lower()
        if choice == CHOICES:
            return choice
        # TODO: if choice is valid, return it
        else:
            print("loop repeats on its own")
        # TODO: otherwise print a message (loop repeats on its own)
        pass


def get_computer_choice():
    """
    Step 2: return a random item from CHOICES.
    Hint: random.choice() picks an item, unlike randint which picks a number.
    """
    computer_choice = random.choice(CHOICES)
    return computer_choice
    # TODO


def decide_winner(player, computer):
    """
    Steps 3 and 4: return "tie", "win", or "lose" from the player's view.
    Check the tie first, then use BEATS for the rest.
    """
    # TODO: tie case
    player = get_player_choice()
    computer = get_computer_choice()
    if player == computer:
        print("tie")
    # TODO: player wins case (use BEATS)
    if player != computer:
        print("player win")
    # TODO: everything else is a loss
    else:
        print("loss")
    pass


def play_round(score):
    """
    Play one round and update `score`, a dict like {"win": 0, "lose": 0, "tie": 0}.
    """
    player = get_player_choice()
    computer = get_computer_choice()
    print(f"You chose {player}, computer chose {computer}.")

    result = decide_winner(player, computer)
    # TODO: Step 5: add 1 to the matching key in `score`
    # TODO: print a message for the result


def main():
    score = {"win": 0, "lose": 0, "tie": 0}
    while True:
        play_round(score)
        print(f"Score: {score['win']} wins, {score['lose']} losses, {score['tie']} ties")

        # TODO: Step 6: ask "play again? (y/n)" and break if the answer is not yes
        # Careful with your condition: think about `and` vs `or`.
        pass


if __name__ == "__main__":
    main()