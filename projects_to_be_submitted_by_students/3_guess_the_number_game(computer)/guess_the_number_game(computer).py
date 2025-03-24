# Import randm module to generate random number
import random


# Function to guess the number
def computer_guess(x):

    # Initialize the range and feedback
    low = 1
    high = x
    feedback = ""

    # Loop to guess the number
    print(f"Think of a number between 1 and {x}, I will try to guess it.")
    
    # Ask for feedback until the guess is correct (feedback == "c")
    while feedback != "c":

        # If the range is not empty, guess a number
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)? "
        ).lower()

        # Check the feedback and adjust the range accordingly
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback != "c":
            print("Invalid input! Please enter H, L, or C.")

    # Print the final message
    print(f"Yay! The computer guessed your number, {guess}, correctly!")


if __name__ == "__main__":
    computer_guess(10)
