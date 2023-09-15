import random
import os
from art import logo

# Function to deal a random card from the deck
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Function to calculate the score of a hand of cards
def calculate_score(cards):
    """Calculates the score of a hand of cards"""
    # Check for a Blackjack (ace + 10)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # Check for an Ace (11). If score is over 21, change Ace to 1.
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Function to compare scores and determine the winner
def compare(user_score, computer_score):
    """Compares the user's and computer's scores to determine the winner"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose. Opponent has a Blackjack."
    elif user_score == 0:
        return "Win with a Blackjack! 😎🎉"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."

# Main game function
def play_game():
    print(logo)
    
    user_cards = []
    computer_cards = []
    is_game_over = False
    
    # Deal initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        # Display user's cards and the computer's first card
        print(f"    Your Cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's First Card: {computer_cards[0]}")
        
        # Check if game should end
        if user_score > 21 or user_score == 0 or computer_score == 0:
            is_game_over = True
        else:
            response = input("\nIf you want to draw another card, type 'y'. If not, type 'n': ")
            if response == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
    
    # Computer's turn
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    # Display final hands and determine the winner
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Start the game
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system("cls")
    play_game()