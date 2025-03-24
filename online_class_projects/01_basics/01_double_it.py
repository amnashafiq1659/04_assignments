# Function to double the number
def squares():

    # Get the user's input and initialize the current value to it.
    curr_value = int(input("Enter a number: "))

    # Print the current value and double it until it reaches 100.
    while curr_value < 100:

        # Double the current value and print it.
        curr_value = curr_value * 2
        print(curr_value)


if __name__ == "__main__":
    squares()
