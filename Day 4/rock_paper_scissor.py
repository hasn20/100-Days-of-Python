# Define the rock, paper, and scissors ASCII art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Import the random module for generating computer's choice
import random

# Get the user's choice as an integer (0 for Rock, 1 for Paper, 2 for Scissors)
user_choice = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors \n"))

# Generate a random choice for the computer (0 for Rock, 1 for Paper, 2 for Scissors)
computer_choice = random.randint(0, 2)

# Create a list of game options for printing
game_list = [rock, paper, scissors]

# Check if the user's input is valid (0, 1, or 2)
if user_choice < 0 or user_choice >= 3:
    print("You entered an invalid number. You lose!")
else:
    # Print the user's and computer's choices using the ASCII art
    print("You chose:")
    print(game_list[user_choice], "\n")
    print("Computer chose:")
    print(game_list[computer_choice])

    # Determine the winner of the game
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (
        (user_choice == 0 and computer_choice == 2)
        or (user_choice == 1 and computer_choice == 0)
        or (user_choice == 2 and computer_choice == 1)
    ):
        print("You win!")
    else:
        print("You lose!")
