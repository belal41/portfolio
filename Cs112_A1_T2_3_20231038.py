# File: Cs112_A1_T2_3_20231038
# Purpose: A two-player game that let you choose a square number less than or equal to number of coins and subtract it from all coins .The first player that gets to 0 wins. There is no draw in this game
# Author: Belal Bakry Ahmed Ali
# ID: 20231038
# Welcome message
print("Welcome to the Subtracting Square game")
import random

def generate_non_square():
    while True:
        num = random.randint(10, 1000)
        if int(num * 0.5 + 0.5) * 2 != num:
            return num

def user_input_square1():
    while True:
        num = input("Please player 1 enter a square number: ")
        if num.isdigit():
            num = int(num)
            if int(num ** 0.5) ** 2 == num:
                return num
            else:
                print("Please enter a square number.")
        else:
            print("Please enter a valid square number")

def user_input_square2():
    while True:
        num = input("Please player 2 enter a square number: ")
        if num.isdigit():
            num = int(num)
            if int(num ** 0.5) ** 2 == num:
                return num
            else:
                print("Please enter a square number.")
        else:
            print("Please enter a valid square number.")

# Choose how to input the number of coins
while True:
    choice = input("Choose 'random' to generate a random number of coins or 'manual' to enter it manually: ")
    if choice.lower() == "random" or choice.lower() == "manual":
        break
    else:
        print("Invalid choice.")

if choice.lower() == "random":
    n_coins = generate_non_square()
elif choice.lower() == "manual":
    while True:
        try:
            n_coins = int(input("Please enter the number of coins (must be positive): "))
            if n_coins > 0:
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid square number")

print("Number of coins =", n_coins)

# Game playing
while n_coins >= 1:
    # Player 1's turn
    while True:
        move = user_input_square1()
        if move > n_coins:
            print("Invalid move! Please choose a number less than or equal to", n_coins)
        else:
            break
    n_coins -= move
    print("Now we have", n_coins, "coins")
    if n_coins <= 0:
        print("Player 1 is the winner!")
        break

    # Player 2's turn
    while True:
        move = user_input_square2()
        if move > n_coins:
            print("Invalid move! Please choose a number less than or equal to", n_coins)
        else:
            break
    n_coins -= move
    print("Now we have", n_coins, "coins")
    if n_coins <= 0:
        print("Player 2 is the winner!")
        break