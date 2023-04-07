from random import random


def play():
    print("This is a TicTacToe-Game. To play press X for player one and O for player two. The game shows you how must choose / starts.")
    print("You can select your field with the numbers.")
    startchooser = random()
    if (startchooser > 0.5):
        print("X starts!")
    elif (startchooser < 0.5):
        print("O starts!")

    print("\n Lets start!")

    print("\n **************************************** \n\n  X # X # X  \n ########### \n X # X # X \n ########### \n X # X # X \n")

    print("")


play()