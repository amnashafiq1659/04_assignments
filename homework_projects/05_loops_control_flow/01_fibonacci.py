# Define the maximum number of the Fibonacci sequence
max_value: int = 10000


# Define the Fibonacci sequence
def fibonacci():

    # Initialize the Fibonacci sequence
    curr_value = 0

    # Initialize the next value
    next_value = 1

    # Print the Fibonacci sequence
    while curr_value <= max_value:

        # Print the current value
        print(curr_value)

        # Calculate the next value
        after_next_value = curr_value + next_value

        # Update the current value
        curr_value = next_value

        # Update the next value
        next_value = after_next_value


if __name__ == "__main__":
    fibonacci()
