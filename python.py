import random

def guess_the_number_game():
    """
    The main function to run the "Guess the Number" game.
    """
    # Ask the user for the upper limit of the number to guess.
    print("Welcome to Guess the Number!")
    print("I will pick a number, and you will try to guess it.")
    
    # Use a loop to make sure the user enters a valid number for the range.
    while True:
        try:
            # Get the upper limit from the user.
            upper_limit = int(input("Please enter the highest number you would like to guess to: "))
            
            # The upper limit must be a positive integer.
            if upper_limit > 0:
                break # Exit the loop if the input is valid.
            else:
                print("Please enter a positive number.")
        except ValueError:
            # Handle cases where the user enters non-integer input.
            print("That's not a valid number. Please try again.")

    # Generate a random integer between 1 (inclusive) and the upper limit (inclusive).
    secret_number = random.randint(1, upper_limit)
    
    # Initialize the number of guesses and the player's guess.
    guesses = 0
    player_guess = 0
    
    # Main game loop. It continues until the player guesses the correct number.
    while player_guess != secret_number:
        try:
            # Prompt the player to make a guess.
            player_guess = int(input(f"Guess a number between 1 and {upper_limit}: "))
            guesses += 1 # Increment the guess counter.
            
            # Check the player's guess.
            if player_guess < secret_number:
                print("Your guess is too low. Try again!")
            elif player_guess > secret_number:
                print("Your guess is too high. Try again!")
            else:
                # The player guessed correctly.
                print(f"Congratulations! You guessed the number {secret_number} in {guesses} tries!")
                break # Exit the loop.
        except ValueError:
            # Handle invalid input (non-integer).
            print("Invalid input. Please enter a number.")
            
    # Check if the player wants to play again.
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == 'yes':
        guess_the_number_game() # Restart the game.
    else:
        print("Thanks for playing!")

# Run the game when the script is executed.
if __name__ == "__main__":
    guess_the_number_game()
