# Print the initial game scene (ASCII art)
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Print game introduction
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Prompt the player to choose a direction
direction = input("You're at a crossroad. Do you want to go left or right? ")

if direction.lower() == 'left':
    # If the player chooses to go left, ask them to swim or wait
    swim_or_wait = input("You come to a lake. Do you want to swim across or wait for a boat? ")
    
    if swim_or_wait.lower() == 'wait':
        # If the player chooses to wait, ask them to choose a door
        door = input("You arrive at an island with three doors - red, blue, and yellow. Which door do you choose? ")
        
        if door.lower() == 'yellow':
            # If the player chooses the yellow door, they win
            print("Congratulations! You have found the treasure. You win!")
        elif door.lower() == 'red':
            # If the player chooses the red door, they are burned by fire and lose
            print("Burned by fire. Game Over.")
        elif door.lower() == 'blue':
            # If the player chooses the blue door, they are eaten by beasts and lose
            print("Eaten by beasts. Game Over.")
        else:
            # If the player chooses any other door, they lose
            print("Game Over.")
    else:
        # If the player chooses to swim, they are attacked by trout and lose
        print("Attacked by trout. Game Over.")
else:
    # If the player chooses to go right, they fall into a hole and lose
    print("Fall into a hole. Game Over.")
