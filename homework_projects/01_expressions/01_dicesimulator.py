# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
num_sides: int = 6


# Function to roll the dice
def roll_dice():

    # Roll the first die
    die1: int = random.randint(1, num_sides)

    # Roll the second die
    die2: int = random.randint(1, num_sides)

    # Calculate the total of the two dice
    total: int = die1 + die2

    # Print the total of the two dice
    print("Total of two dice:", total)


# Main function to run the program
def main():

    # Initialize the first die
    die1: int = 10

    # Print the first die
    print(f"die1 in main() starts as: {die1}")

    # Roll the dice
    roll_dice()
    roll_dice()
    roll_dice()

    # Print the first die
    print(f"die1 in main() is: {die1}")


if __name__ == "__main__":
    main()
