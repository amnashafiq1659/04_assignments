# Function to divide two integers and print the result
def divide():

    # Prompt the user to enter an integer to be divided
    divider: int = int(input("Please enter an integer to be divided: "))

    # Prompt the user to enter an integer to divide by
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Calculate the quotient of the division
    quotient: int = divider // divisor

    # Calculate the remainder of the division
    remainder: int = divider % divisor

    # Print the result of the division
    print(f"The result of the division is {quotient} with a remainder of {remainder}.")


if __name__ == "__main__":
    divide()
