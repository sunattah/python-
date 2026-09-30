"""
Rock, Paper, Scissors
---------------------
Rules:
- The player and the computer each pick rock, paper, or scissors.
- rock beats scissors, scissors beats paper, paper beats rock.
- Same choice on both sides is a tie.
- Keep a running score (wins, losses, ties) across rounds.
- Ask to play again after each round.
"""

import random

# All valid game choices
CHOICES = ["rock", "paper", "scissors"]

# Dictionary defining what each choice defeats
BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}


def get_player_choice():
    """
    Step 1: keep asking until the player types a valid choice.
    Return the choice as a lowercase string.
    """
    while True:
        choice = input("rock, paper, or scissors? ").strip().lower()
        
        # Correctly check if the choice exists in the list
        if choice in CHOICES:
            return choice  # Sends the choice to the game and breaks the loop
        
        # If the choice is invalid, print a message and the loop repeats
        print("Invalid choice! Please type rock, paper, or scissors.")


def get_computer_choice():
    """
    Step 2: return a random item from CHOICES.
    """
    return random.choice(CHOICES)


def decide_winner(player, computer):
    """
    Steps 3 and 4: return "tie", "win", or "lose" from the player's view.
    """
    # 1. Check for a tie first
    if player == computer:
        return "tie"
        
    # 2. Check if the player wins using the BEATS dictionary
    if BEATS[player] == computer:
        return "win"
        
    # 3. If it's not a tie and the player didn't win, the computer won
    return "lose"


def play_round(score):
    """
    Play one round and update `score`.
    """
    player = get_player_choice()
    computer = get_computer_choice()
    print(f"You chose {player}, computer chose {computer}.")

    result = decide_winner(player, computer)
    
    score[result] += 1
    
    if result == "win":
        print("🎉 You won this round!")
    elif result == "lose":
        print("😢 The computer won this round.")
    else:
        print("🤝 It's a tie!")
        
    return score


def main():
    score = {"win": 0, "lose": 0, "tie": 0}
    while True:
        play_round(score)
        print(f"Score: {score['win']} wins, {score['lose']} losses, {score['tie']} ties\n")

        again = input("Play again? (y/n): ").strip().lower()
        
        if again != 'y' and again != 'yes':
            print("\nThanks for playing! Final Score:")
            print(f"{score['win']} Wins | {score['lose']} Losses | {score['tie']} Ties")
            break


if __name__ == "__main__":
    main()
