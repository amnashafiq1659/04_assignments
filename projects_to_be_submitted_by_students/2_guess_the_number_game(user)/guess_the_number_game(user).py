# Import random module to generate random number
import random


# Function to generate random number and take user input to guess the number
def user_guess(x):

    # Generate random number between 1 to x
    random_number = random.randint(1, x)

    # Initialize guess and attempt
    guess = 0
    attempt = 0

    # Welcome message
    print("Welcome to 'Guess the Number Game'! 🎉\n")

    # Take user input to guess the number
    while guess != random_number:

        # Check user input and update attempts based on guess
        try:
            guess = int(input(f"Guess a number between 1 to {x}: "))
            attempt += 1
            if guess < random_number:
                print("Too low! Try again. ⬆️")
            elif guess > random_number:
                print("Too high! Try again. ⬇️")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Print message if user guessed the number correctly
    print(
        f"\n🎉Yay, congrats. You have guessed the number {random_number} correctly in {attempt} attempts."
    )

    print("\nThanks for playing! 👋")


if __name__ == "__main__":
    user_guess(20)
