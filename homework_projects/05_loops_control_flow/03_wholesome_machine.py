# Define the affirmation
affirmation: str = "I believe in myself and my abilities."


# Define the function
def wholesome_machine():

    # Ask the user to input the affirmation
    print(f"Please type the following affirmation: {affirmation}")

    # Get the user's input
    feedback = input()

    # Check if the user's input is the affirmation
    while feedback != affirmation:
        print("That's not the affirmation.")

        # Ask the user to input the affirmation again
        print(f"Please type the following affirmation: {affirmation}")
        feedback = input()

    # If the user's input is the affirmation, print a message
    print("That's right... You're doing great!")


if __name__ == "__main__":
    wholesome_machine()
