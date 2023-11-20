# create a minigame that will be played in the terminal and follow the rules of the game
#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#By the end of each round, the player can choose whether to play again.
#Display the player's score at the end of the game.
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

# Importing the random module
import random

# Defining the game's rules
rules = {
    "rock": {"scissors": "crushes", "paper": "is covered by"},
    "paper": {"rock": "covers", "scissors": "is cut by"},
    "scissors": {"paper": "cuts", "rock": "is crushed by"}
}

# Defining the game's options
options = ["rock", "paper", "scissors"]

# Defining the game's messages
messages = {
    "tie": "It's a tie!",
    "win": "You win!",
    "lose": "You lose!",
    "invalid": "Invalid option!"
}

# Defining the game's functions
def get_user_option():
    """Get the user's option."""
    option = input("Choose rock, paper, or scissors: ")
    return option.lower()

def get_computer_option():
    """Get the computer's option."""
    option = random.choice(options)
    return option

def get_winner(user_option, computer_option):
    """Get the winner of the round."""
    if user_option == computer_option:
        return "tie"
    elif rules[user_option][computer_option] == "crushes":
        return "win"
    elif rules[user_option][computer_option] == "is covered by":
        return "lose"
    elif rules[user_option][computer_option] == "covers":
        return "win"
    elif rules[user_option][computer_option] == "is cut by":
        return "lose"
    elif rules[user_option][computer_option] == "cuts":
        return "win"

def print_result(user_option, computer_option, result):
    """Print the result of the round."""
    if result == "tie":
        print(f"{messages['tie']} Both players selected {user_option}.")
    elif result == "win":
        print(f"{messages['win']} {user_option} {rules[user_option][computer_option]} {computer_option}.")
    elif result == "lose":
        print(f"{messages['lose']} {computer_option} {rules[user_option][computer_option]} {user_option}.")
    else:
        print(messages['invalid'])

def play_again():
    """Ask the user if they want to play again."""
    answer = input("Do you want to play again? (y/n) ")
    return answer.lower() == "y"

def print_score(score):
    """Print the score of the game."""
    print(f"Your score is: {score}")

# Defining the game's main function
def main():
    # Defining the game's variables
    score = 0
    playing = True

    # Playing the game
    while playing:
        # Getting the user's option
        user_option = get_user_option()

        # Getting the computer's option
        computer_option = get_computer_option()

        # Getting the winner of the round
        result = get_winner(user_option, computer_option)

        # Printing the result of the round
        print_result(user_option, computer_option, result)

        # Updating the score
        if result == "win":
            score += 1
        elif result == "lose":
            score -= 1

        # Printing the score
        print_score(score)

        # Asking the user if they want to play again
        playing = play_again()

# Calling the main function
main()
