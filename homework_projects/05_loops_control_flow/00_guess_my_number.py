# import random module to generate a random number
import random


# Function to play the game
def main():

    # Generate a random number
    secret_number = random.randint(1, 99)

    # Print the instructions
    print("I'm thinking of a number between 1 and 99.")

    # Get the user's guess
    guess = int(input("Enter a guess: "))

    # Check if the guess is correct
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

        print()
        # Get a new guess
        guess = int(input("Enter a new guess: "))

    # Print a congratulatory message
    print(f"Congratulations! The number was {secret_number}.")


if __name__ == "__main__":
    main()
