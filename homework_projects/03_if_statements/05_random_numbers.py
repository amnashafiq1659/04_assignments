# Import a random module to generate random numbers
import random

# Define the number of random numbers to generate
number: int = 10

# Define the minimum and maximum values for the random numbers
min_value: int = 1
max_value: int = 100


# Function to generate random numbers
def random_number():

    # Generate the specified number of random numbers within the given range
    for n in range(number):

        # Generate a random numbers between min_value and max_value
        random_number = random.randint(min_value, max_value)

        # Print the random numbers
        print(random_number,end=" ")


if __name__ == "__main__":
    random_number()
