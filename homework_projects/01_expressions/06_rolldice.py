# Import the random library
import random

# Define the number of sides on the dice
num_sides: int = 6


# Function to roll the dice
def roll_dice():

    # Roll the first die
    die1: int = random.randint(1, num_sides)

    # Roll the second die
    die2: int = random.randint(1, num_sides)

    # Calculate the total of the two dice
    total: int = die1 + die2

    # Print the result
    print(f"Dice have {num_sides} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")


if __name__ == "__main__":
    roll_dice()
