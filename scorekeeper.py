# yu-gi-oh scorekeeper // scorekeeper.py

from __future__ import print_function
import random

player1 = ""
player2 = ""
player1_points = 0
player2_points = 0
starting_points = 0


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


def setup():
    # print("This is the game function.")
    global player1, player2, starting_points, player1_points, player2_points
    player1 = raw_input("What is player 1's name? ")
    if player1 == "":
        print("You didn't enter a name for player 1! Please try again.")
        setup()
    else:
        player2 = raw_input("What is player 2's name? ")
        if player2 == "":
            print("You didn't enter a name for player 2! Please try again.")
            setup()
        else:
            starting_points = int(raw_input(
                    "How many life points would you like to start with? "))
            if type(starting_points) != int:
                print("That is not a number! Please start again.")
            else:
                print(
                    "Player 1 is " + player1 +
                    " and player 2 is " + player2 +
                    ". The starting number of life points is " +
                    str(starting_points) + ".")
                player1_points = starting_points
                player2_points = starting_points
                begin()


def begin(choice=""):
    choice = raw_input(
        "Would you like to begin? Type 'yes' to begin the game or" +
        " type 'no' to return to the main menu: ")
    if choice.lower() == "no":
        main_menu()
    elif choice.lower() == "yes":
        player_order()
    else:
        print("That is not a valid option, please try again.")
        begin()


def player_order(going_first="", choice=0):
    # print("This is the game function.")
    choice = raw_input(
        "Would you like to decide which player goes first or would you like" +
        " me to flip a coin? Please select an option: \n" +
        "1: We will choose \n" +
        "2: Flip a coin for me \n")
    if choice == "1":
        going_first = choosing_first_player()
    elif choice == "2":
        going_first = flipping_for_first_player()
    else:
        print("That is not a valid option, please choose again.")
        player_order()
    return going_first


def coin_flip(coin=0, result=""):
    coin = random.random()
    if coin >= 5:
        result = "heads"
    else:
        result = "tails"
    return result


def choosing_first_player(choice=0):
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
        choosing_first_player()
    return choice


def flipping_for_first_player(flipped_coin=""):
    flipped_coin = coin_flip()
    if flipped_coin == "heads":
        going_first = player1
    else:
        going_first = player2
    print("The result of the coin flip is: " + flipped_coin)
    print(going_first + " is going first.")
    return going_first


def game(choice=0):
    choice = raw_input(
        "What would you like to do? Please select an option: " +
        "\n1: Add/remove life points from " + player1 +
        "\n2: Add/remove life points from " + player2 +
        "\n3: View current life points" +
        "\n4: Go back to the main menu (end game)")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    elif choice == "4":
        pass
    else:
        print("That is not a valid choice, please choose again.")
        game()


def player1_points(choice=0):
    print(
        "Would you like to add or remove points from " + player1 + "?\n" +
        "Please select an option: \n" +
        "1: Add points\n" +
        "2: Remove points\n" +
        "3: Neither, take me back to the previous menu.")
    if choice == "1":
        pass
    elif choice == "2":
        pass
    elif choice == "3":
        pass
    else:
        print("That is not a valid choice, please choose again.")


def about():
    print("This is the about function.")


def close():
    print("This is the close function.")

main_menu()
