import random

tries = 1
MIN_VALUE = 1
MAX_VALUE = 10
high_score = MAX_VALUE
high_score_name = 'CODE MAN'

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
            their_number = int(input("\nPick a number between 1-10:    "))


            # Provide Correct Feedback
            if their_number < 1 or their_number > 10:
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