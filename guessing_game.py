"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""


# Import the random module.
import random
# Create the start_game function.
def start_game():
    tries = 0
# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
    print("---WELCOME TO THE GUESS YOUR NUMBER GAME---")
#   2. Store a random number as the answer/solution.
    random_number = random.randint(1,10)
#   3. Continuously prompt the player for a guess.
    while True:
        try:
            their_number = int(input("\nPick a number between 1-10:    "))
            if their_number < 1 or their_number > 10:
                print("\nThat number is out of range. Pick a number between 1-10.")

            else:
                tries += 1
                break
        
        except ValueError:
            print("I need a number between 1 and 10 please.")
        



    while True:





        if their_number > random_number:
            their_number = int(input("\nThe number is lower, try again!\nPick another number 1-10:   "))
            tries += 1

        if their_number < random_number:
            their_number = int(input("\nThe number is higher, try again!\nPick another number 1-10:   "))
            tries += 1

        else:
            print(f"\nYou got it! The number was {random_number}! You got it in {tries} attempts!")


            play_again = input("Do you want to play again? y/n  ")
                               
            if play_again.lower() == 'y':
                start_game()
            else:
                print("\nTHANKS FOR PLAYING! :)\n")
                break

start_game()
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
