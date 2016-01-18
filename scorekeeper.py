# yu-gi-oh scorekeeper // scorekeeper.py

from __future__ import print_function
import random


def main_menu():
    choice = 0
    print(
        "Welcome to Deven's Yu-Gi-Oh score keeper! Please select an option:"
         )
    print(
        "1: New game \n"
        "2: About \n"
        "3: Close \n"
         )
    choice = raw_input()
    if choice == "1":
        setup()
    elif choice == "2":
        about()
    elif choice == "3":
        close()
    else:
        print("That is not a valid option, please choose again.")
        main_menu()


def setup(player1="", player2="", starting_points=0):
    # print("This is the game function.")
    global player1, player2, starting_points
    player1 = raw_input("What is player 1's name? ")
    player2 = raw_input("What is player 2's name? ")
    starting_points = raw_input(
            "How many life points would you like to start with?"
            )
    print(
        "Player 1 is " + player1 + " and player 2 is " + player2 +
        ". The starting number of life points is " + starting_points + ".")
    return player1, player2, starting_points
    begin()


def begin(choice=""):
    choice = raw_input(
        "Would you like to begin? Type 'yes' to begin the game or" +
        " type 'no' to return to the main menu: ")
    if choice.lower() == "no":
        main_menu()
    elif choice.lower() == "yes":
        game()
    else:
        print("That is not a valid option, please try again.")
        begin()


def game(going_first, flipped_coin, choice=0):
    # print("This is the game function.")
    choice = raw_input(
        "Would you like to decide which player goes first or would you like" +
        " me to flip a coin? Please select an option: \n" +
        "1: We will choose \n" +
        "2: Flip a coin for me \n")
    if choice == "1":
        going_first = first_player()
    elif choice == "2":
        flipped_coin = coin_flip()
        if flipped_coin == "heads":
            going_first = player1
        else:
            going_first = player2
        print("The result of the coin flip is: " + flipped_coin)
        print(going_first + " is going first.")
    else:
        print("That is not a valid option, please choose again.")
        game()


def coin_flip(coin, result):
    coin = random.random()
    if coin >= 5:
        result = "heads"
    else:
        result = "tails"
    return result


def first_player(choice):
    choice = raw_input(
        "Please choose which player will go first: \n" +
        "1: Player 1 \n" +
        "2: Player 2 \n")
    if choice == "1":
        choice = player1
    elif choice == "2":
        choice = player2
    else:
        print("That is not a valid option, please choose again.")
        first_player
    return choice


def about():
    print("This is the about function.")


def close():
    print("This is the close function.")

main_menu()
