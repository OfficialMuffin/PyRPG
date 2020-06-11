"""
    Python RPG
    by OfficialMuffin
"""

import game
import player

game.intro()

try:
    print("Please answer the following questions.\n")
    username = (input("Enter your username: "))

    player1 = player.Player(username)

    print("------------------------")
    print("Your username is: ", player1.getName())
    print("Are these correct? (Y/n)")
    correct = input()
    if correct == 'Y':
        print("Great!")
    elif correct == 'n':
        print("Try again...")
    else:
        print("Invalid Input!")
    print("------------------------")

    # DEBUGGING
    # print("Username is", player1.getName(), "Age is", player1.getAge())

except ValueError:
    pass
