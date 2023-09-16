from random import randint
import os

# Initialize game variables
LEVEL = 0
NUMBER_TO_BE_GUESSED = randint(1, 100)

# Function to check the user's guess and return remaining guesses
def check():
    global LEVEL
    guess = int(input("Make a guess: "))
    
    if guess > NUMBER_TO_BE_GUESSED:
        print("\nToo high.")
        LEVEL -= 1
        return LEVEL
    elif guess < NUMBER_TO_BE_GUESSED:
        print("\nToo low.")
        LEVEL -= 1
        return LEVEL
    elif guess == NUMBER_TO_BE_GUESSED:
        print("\nYou have guessed right! You Won!")
        return guess
    elif guess > 100 or guess < 0:
        print("\nOut of Bounds")
        LEVEL -= 1
        return LEVEL

# Function to play the game
def play_game():
    global LEVEL
    from art import logo  # Import the game logo from art module
    print(logo)
    print("Welcome To The Number Guessing Game!")
    print("Think of a Number between 1 and 100")
    
    input_check_1 = True
    while input_check_1:
        difficulty_level = input("Choose Difficulty type 'easy' or 'hard': ")
        
        if difficulty_level == "easy":
            LEVEL = 10
            input_check_1 = False
            while LEVEL != 0:
                remaining_guess = check()
                if remaining_guess == NUMBER_TO_BE_GUESSED:
                    LEVEL = 0
                elif remaining_guess == 0:
                    print("You've run out of guesses. You lose.")
                else:
                    print(f"You have {remaining_guess} attempts remaining to guess the number!")
        
        elif difficulty_level == "hard":
            input_check_1 = False
            LEVEL = 5
            while LEVEL != 0:
                remaining_guess = check()
                if remaining_guess == NUMBER_TO_BE_GUESSED:
                    LEVEL = 0
                elif remaining_guess == 0:
                    print("You've run out of guesses. You lose.")
                else:
                    print(f"You have {remaining_guess} attempts remaining to guess the number!")
        else:
            print("Wrong Entry. Enter again")

# Main game loop
play = input("Do You Want to play The Number Guessing Game! type 'yes' or 'no': ")
if play == "yes":
    play_game()
    a = True
    while a:
        again_check = input("Do you want to play again? type 'yes' or 'no': ")
        if again_check == "no":
            os.system("cls")
            a = False
        elif again_check == "yes":
            play_game()