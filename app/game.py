 
from random import choice

#
# USER SELECTION
#

VALID_OPTIONS = ["rock", "paper", "scissors"]

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
if u == c:
    print("It's a tie!")

elif (u == "rock" and c == "paper") or (u == "paper" and c == "scissors") or (u == "scissors" and c == "rock"):
    print("The computer wins")

elif (u == "rock" and c == "scissors") or (u == "paper" and c == "rock") or (u == "scissors" and c == "paper"):
    print("The user wins")
