"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""


# Import the random module.
# Create the start_game function.
# Write your code inside this function.
#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.


import random

tries = 1
MIN_VALUE = 1
MAX_VALUE = 10
high_score = MAX_VALUE
high_score_name = 'PYGUY'

def start_game():
    
    global high_score_name
    global high_score

    # Provide a Welcome Message
    print("\n---WELCOME TO THE GUESS YOUR NUMBER GAME---")

    # High Score at start of a new game
    print(f"\nThe high score is {high_score} achieved by {high_score_name}!\n")
    
    # Get name for high score
    name = input("What is your name?    ")

    # Generate the Winning Number
    random_number = random.randint(MIN_VALUE,MAX_VALUE)

    # Continuous Guess Prompting
    while True:

        try:
            global tries
            their_number = int(input(f"\nPick a number between {MIN_VALUE} and {MAX_VALUE}:    "))


            # Provide Correct Feedback
            if their_number < MIN_VALUE or their_number > MAX_VALUE:
                print("\nThat number is out of range.")

            elif their_number > random_number:
                print("\nThe number is lower, try again!")
                tries += 1

            elif their_number < random_number:
                print("\nThe number is higher, try again!")
                tries += 1
            
            else:
                # Display the Score
                print(f"\nYou got it {name}! The number was {random_number}! You got it in {tries} attempts!")

                # Change high score and high score name if its better than the old one
                if tries < high_score:
                    high_score_name = name
                    high_score = tries


                play_again = input("Do you want to play again? y/n  ")
               
                # Play again prompt
                if play_again.lower() == 'y':
                    tries = 1
                    start_game()
                    break

                else:
                    # Provide a Goodbye Message
                    print("\nTHANKS FOR PLAYING! :)\n")
                    break

        except ValueError:
            # Handle Errors and Exceptions
            print(f"I need a whole number, come on you got this {name}.")
        
start_game()