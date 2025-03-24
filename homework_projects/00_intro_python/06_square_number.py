# This function prompts the user to enter a number and then displays its square.
def square_number():

    # Prompt the user to enter a number.
    number: float = float(input("Type a number to see its square: "))

    # Calculate the square of the number.
    squared: float = number * number

    # Display the square of the number.
    print(f"{number} squared is {squared}")


if __name__ == "__main__":
    square_number()
