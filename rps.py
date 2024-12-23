# rock paper scissor

import random

choices = [
    'rock',
    'paper',
    'scissor',
]

user_still_wants_to_play = True

while (user_still_wants_to_play):

    computor_choice = random.choice(choices)

    user_input = input("Rock or Paper or Scissor:")

    if (user_input not in choices):
        print("invalid input")
        quit()

    if (user_input == computor_choice):
        print("Tie")

    elif (
        (user_input == 'rock' and computor_choice == 'scissor')
        or (user_input == 'scissor' and computor_choice == 'paper')
        or (user_input == 'paper' and computor_choice == 'rock')
    ):
        print("You won")

    else:


        print("you loose")
    want_to_play = input("Do you still want to play y/n: ")
    user_still_wants_to_play = want_to_play =='y'

    