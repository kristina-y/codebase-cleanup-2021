 
from random import choice

VALID_OPTIONS = ["rock", "paper", "scissors"]

def determine_winner(choice1, choice2):
    """
    This function determines the winner of a rock, paper, scissors game, given 2 inputs
    
    Params:
        Choice1 and Choice2 are string that are within the VALID_OPTIONS array

    Examples:
        determine_winner(rock, paper)
        determine_winner(scissors, rock)
    """
    # This strategy was adapted from Professor Rossetti's in-class walk-through
    winners = {
        "rock":{
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper":{
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors":{
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        },
    }
    winning_choice = winners[choice1][choice2]
    return winning_choice


if __name__ == "__main__":
    #
    # USER SELECTION
    #


    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in VALID_OPTIONS:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(VALID_OPTIONS)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #
    winner = determine_winner(u,c)

    if winner == u:
        print("You won")
    elif winner == c:
        print("Computer won")
    elif winner == NONE:
        print("You tied with the computer")
