from art import logo
from art import vs
from game_data import data
import random
import os


def vs_check(n1, n2, score):
    print(logo)

    dictionary = data[n1]
    name_1 = dictionary["name"]
    follower_count_1 = dictionary["follower_count"]
    description_1 = dictionary["description"]
    country_1 = dictionary["country"]

    dictionary = data[n2]
    name_2 = dictionary["name"]
    follower_count_2 = dictionary["follower_count"]
    description_2 = dictionary["description"]
    country_2 = dictionary["country"]

    print(f"Compare A: {name_1}, a {description_1}, from {country_1} ")
    print(vs)
    print(f"against B: {name_2}, a {description_2}, from {country_2} ")

    correct = True

    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_input == "a":
        if follower_count_1 > follower_count_2:
            score += 1
        else:
            correct = False
    elif user_input == "b":
        if follower_count_2 > follower_count_1:
            score += 1
        else:
            correct = False

    return score, correct


Check = True
Score = 0

# Initialize the index for the first celebrity
N1 = random.randint(0, len(data) - 1)

while Check:
    # Generate a new random index for N2
    N2 = random.randint(0, len(data) - 1)
    while N1 == N2:  # Ensure N1 and N2 are different
        N2 = random.randint(0, len(data) - 1)

    Score, Correct = vs_check(N1, N2, Score)

    os.system("cls")
  
    if Correct:
        print(f"You're right! Current score is {Score}")
        N1 = N2  # Update N1 only if the answer is correct
    else:
        print(f"Sorry that's wrong! Your final score is {Score}")
        Check = False