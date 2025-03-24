# Import random module to generate random numbers
import random

# Define the likelihood of the chaotic counting algorithm to stop
done_likelihood = 0.3


# Define the chaotic counting function
def chaotic_counting():

    # Loop through the numbers from 1 to 10
    for i in range(10):
        # Get the current number and check if the algorithm should stop
        curr_num = i + 1
        # If the algorithm should stop, return from the function
        if done():
            return
        # Print the current number
        print(curr_num)


# Define the done function to check if the algorithm should stop
def done():
    # Return True if a random number is less than the done_likelihood
    return random.random() < done_likelihood


# Define the main function
def main():
    # Print the instructions to the user
    print(
        "I'm going to count until 10 or until I feel like stopping, whichever comes first."
    )
    chaotic_counting()
    print("I'm done.")


if __name__ == "__main__":
    main()
